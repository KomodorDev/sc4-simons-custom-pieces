"""One-folder graphical front end for the existing verified installation APIs."""
from __future__ import annotations

import datetime
import json
import os
from pathlib import Path
import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import traceback

from scp.catalog import load_catalog
from .service import (InstallationCancelled, PlayerDataSelectionRequired,
                      all_implemented_ids, run_install, undo_install)
from .ui_support import default_work_root, progress_text, require_game_closed


class InstallerApp:
    def __init__(self, window, root, info, work_root=None):
        self.window, self.root, self.info = window, Path(root), info
        self.work_root = Path(work_root or default_work_root()).resolve()
        self.events, self.cancelled = queue.Queue(), threading.Event()
        self.busy, self.cancellable = False, False
        self.folder, self.status = tk.StringVar(), tk.StringVar(value="Choose your SimCity 4 game folder to begin.")
        self.detail = tk.StringVar(value="")
        implemented = set(all_implemented_ids(self.root))
        self.names = {piece["id"]: piece["name"] for piece in load_catalog(self.root)["pieces"]
                      if piece["id"] in implemented}
        self.log_file = None
        self.player_data, self.player_candidates = None, []
        self.player_label = tk.StringVar()
        window.title("Simon's Custom Pieces Installer")
        window.geometry("740x455")
        window.minsize(640, 430)
        window.protocol("WM_DELETE_WINDOW", self.close)
        outer = ttk.Frame(window, padding=24)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="Simon's Custom Pieces", font=("Segoe UI", 20, "bold")).pack(anchor="w")
        ttk.Label(outer, text=f"Install all {len(self.names)} implemented pieces", font=("Segoe UI", 12)).pack(anchor="w", pady=(5, 10))
        ttk.Label(outer, text="Requires SimCity 4 Deluxe and the supported NAM 50 right-hand-traffic installation.\nExperimental build: use a test city.", wraplength=680).pack(anchor="w")
        selection = self.selection_row = ttk.Frame(outer)
        selection.pack(fill="x", pady=(24, 12))
        ttk.Entry(selection, textvariable=self.folder, state="readonly").pack(side="left", fill="x", expand=True)
        self.choose_button = ttk.Button(selection, text="Choose game folder…", command=self.choose)
        self.choose_button.pack(side="right", padx=(10, 0))
        self.player_row = ttk.Frame(outer)
        self.player_button = ttk.Button(self.player_row, text="Choose Plugins folder…", command=self.choose_player_data)
        self.player_button.pack(side="left")
        ttk.Label(self.player_row, textvariable=self.player_label, wraplength=400).pack(side="left", padx=(10, 0))
        ttk.Label(outer, textvariable=self.status, wraplength=680).pack(anchor="w", pady=(10, 8))
        self.bar = ttk.Progressbar(outer, mode="indeterminate")
        self.bar.pack(fill="x")
        ttk.Label(outer, textvariable=self.detail, wraplength=680).pack(anchor="w", pady=(10, 8))
        controls = ttk.Frame(outer)
        controls.pack(side="bottom", fill="x", pady=(12, 0))
        self.install_button = ttk.Button(controls, text="Install", command=self.start, state="disabled")
        self.install_button.pack(side="right")
        self.cancel_button = ttk.Button(controls, text="Cancel", command=self.cancel, state="disabled")
        self.cancel_button.pack(side="right", padx=(0, 10))
        self.log_button = ttk.Button(controls, text="Open log", command=self.open_log, state="disabled")
        self.log_button.pack(side="left")
        self.undo_button = ttk.Button(controls, text="Undo last installation", command=self.undo)
        self.undo_button.pack(side="left", padx=(10, 0))
        self.undo_button.configure(state="disabled")
        window.after(100, self.poll)

    def choose(self):
        selected = filedialog.askdirectory(title="Select your SimCity 4 game folder", mustexist=True,
                                           initialdir=self.folder.get() or str(Path.home()))
        if selected:
            self.folder.set(selected)
            self.player_data, self.player_candidates = None, []
            self.player_row.pack_forget()
            self.install_button.configure(state="normal")
            saved = self.work_root / "last-installation.json"
            self.undo_button.configure(state="normal" if saved.is_file() else "disabled")
            self.status.set("Ready to install. Close SimCity 4, then select Install.")
            self.detail.set("The installer will find Plugins, prepare the pieces, and save a backup automatically.")

    def choose_player_data(self):
        initial = Path(self.player_candidates[0]).parent if self.player_candidates else Path.home()
        selected = filedialog.askdirectory(title="Select the SimCity 4 player-data or Plugins folder you use",
                                           mustexist=True, initialdir=str(initial))
        if selected:
            self.player_data = selected
            self.player_label.set(selected)
            self.status.set("Player-data folder selected. Select Install to continue.")
            self.detail.set("Your original game folder is kept. The installer will verify this Plugins folder before changing it.")

    def start(self):
        self._start_worker(False)

    def undo(self):
        if messagebox.askyesno("Undo last installation", "Restore the state before your last SCP installation?\n\nClose the game first. If this removes newly added pieces, remove those pieces from saved cities before continuing."):
            self._start_worker(True)

    def _start_worker(self, undo):
        if self.busy or not self.folder.get():
            return
        try:
            require_game_closed()
            logs = self.work_root / "logs"
            logs.mkdir(parents=True, exist_ok=True)
            stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
            self.log_file = logs / f"installer-{stamp}.log"
            self.log_file.write_text(json.dumps({"installer": self.info, "action": "undo" if undo else "install",
                                                  "selected_folder": self.folder.get()}) + "\n", encoding="utf-8")
        except (OSError, ValueError) as error:
            self.status.set(str(error))
            return
        self.busy, self.cancellable = True, not undo
        self.cancelled.clear()
        for button in (self.install_button, self.choose_button, self.undo_button, self.player_button):
            button.configure(state="disabled")
        self.cancel_button.configure(state="normal" if self.cancellable else "disabled")
        self.log_button.configure(state="normal")
        self.bar.start(15)
        self.detail.set("The first build can take some time. You can keep this window open while it works.")
        selected, player_data = self.folder.get(), self.player_data

        def progress(event):
            if event.get("phase") in {"install", "undo"}:
                require_game_closed()
            self.events.put(("progress", event))

        def worker():
            try:
                if undo:
                    result = undo_install(self.root, selected, self.work_root, progress=progress,
                                          player_data=player_data)
                else:
                    result = run_install(self.root, selected, self.work_root, progress=progress,
                                         cancel=self.cancelled.is_set, player_data=player_data)
                self.events.put(("undone" if undo else "success", result))
            except PlayerDataSelectionRequired as error:
                self.events.put(("error", {"error": str(error), "player_data_needed": True,
                                           "candidate_paths": error.candidate_paths}))
            except InstallationCancelled as error:
                self.events.put(("cancelled", {"error": str(error)}))
            except Exception as error:
                self.events.put(("error", {"error": str(error), "traceback": traceback.format_exc()}))

        threading.Thread(target=worker, name="scp-install-worker", daemon=False).start()

    def poll(self):
        try:
            while True:
                kind, value = self.events.get_nowait()
                if self.log_file:
                    try:
                        with self.log_file.open("a", encoding="utf-8") as stream:
                            stream.write(json.dumps({"event": kind, "detail": value}) + "\n")
                    except OSError:
                        # A logging failure must not lose the worker's final
                        # result or leave the window permanently disabled.
                        self.log_file = None
                        self.log_button.configure(state="disabled")
                if kind == "progress":
                    self.status.set(progress_text(value, self.names))
                    if value.get("phase") in {"install", "undo", "complete"}:
                        self.cancellable = False
                        self.cancel_button.configure(state="disabled")
                    if value.get("phase") == "selection":
                        self.detail.set("Plugins: " + value["plugins"])
                    continue
                self.busy, self.cancellable = False, False
                self.bar.stop()
                self.cancel_button.configure(state="disabled")
                self.choose_button.configure(state="normal")
                self.player_button.configure(state="normal")
                self.install_button.configure(state="normal")
                self.undo_button.configure(state="normal" if (self.work_root / "last-installation.json").is_file() else "disabled")
                if kind == "success":
                    self.status.set(f"Installed — {value['pieces']} pieces are ready.")
                    self.detail.set("Start SimCity 4 and open Transportation → Rail. The trumpet has one assembly button; Tab selects its components. A backup was saved automatically.")
                    if value.get("recovery_record_warning"):
                        self.undo_button.configure(state="disabled")
                        self.detail.set("Installation succeeded and its backup is saved, but Windows could not save the Undo shortcut. Open the log for the recovery details.")
                elif kind == "undone":
                    self.status.set("The previous installation was restored.")
                    self.detail.set("Your game and NAM source files were preserved.")
                else:
                    self.status.set("Cancelled" if kind == "cancelled" else "Installation stopped")
                    self.detail.set(value["error"])
                    if value.get("player_data_needed"):
                        self.player_candidates = value["candidate_paths"]
                        self.player_row.pack(fill="x", after=self.selection_row, pady=(0, 4))
        except queue.Empty:
            pass
        self.window.after(100, self.poll)

    def cancel(self):
        if self.busy and self.cancellable:
            self.cancelled.set()
            self.cancel_button.configure(state="disabled")
            self.detail.set("Cancelling after the current build step. The installed pieces will remain unchanged.")

    def open_log(self):
        if self.log_file and self.log_file.is_file():
            try:
                os.startfile(str(self.log_file))
            except OSError as error:
                messagebox.showerror("Open log", str(error))

    def close(self):
        if self.busy:
            if self.cancellable:
                self.cancel()
            messagebox.showinfo("Installation in progress", "Please wait for the current operation to finish before closing this window.")
        else:
            self.window.destroy()


def smoke_test(root, info, work_root):
    window = tk.Tk()
    try:
        window.withdraw()
        app = InstallerApp(window, root, info, work_root)
        window.update_idletasks()
        window.update()
        if str(app.install_button["state"]) != "disabled" or not app.names:
            raise ValueError("The installer did not start in its expected initial state.")
        return {"status": "passed", "tk_runtime": window.tk.call("info", "patchlevel"),
                "graphical_window_created": True, "implemented_pieces": len(app.names),
                "installation_started": False}
    finally:
        window.destroy()


def run(root, info):
    window = tk.Tk()
    InstallerApp(window, root, info)
    window.mainloop()
