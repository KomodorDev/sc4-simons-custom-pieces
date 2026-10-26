#!/usr/bin/env python3
"""Add the diagonal smooth T without changing the accepted straight example."""
from scp_hsr_tools.register_directional_t import register_examples


def main():
    from scp_hsr.directional_diagonal_t import INFO,RECIPES
    register_examples(INFO,RECIPES,'redesigned-diagonal-junction-example')


if __name__=='__main__':main()
