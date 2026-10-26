HippoTank Demand Fix


PART OF THE HippoTank Bugfix Bundle

THis is just the fix for the demand values for the Medical Clinic, Solar Power Plant, Nuclear Power Plant.

For bundle with other fixes (Industrial High Tech demand, Opera House, Space Port and Crime issues) please see my bundle!




What is actually happening
----------------------------------------------



> the game creates demand for a particular bracket of job but does not actually employ them.

-link: forum thread 	 :: http://sc4devotion.com/forums/index.php?topic=8870.0

> The reason for this is because of a bug. In SimCity 4 the buildings that create demand (available jobs) does so by separating them by wealth bracket. There will be a certain about of jobs available for $ sims, $$ sims, and $$$ sims. This is displayed in a ratio. E.g. crude example- 20:50:30 means there are 20 jobs avialable for $ sims, 50 jobs for $ sims and 30 jobs for $$$ sims.

> The bug occurs when the data in game has two ratios with the same value. It causes the game to ignore one of the values. High Tech Industry has the ratio 10:80:10, and as a result of this bug it causes the $$$ part of the ratio to be ignored resulting in no $$$ sims being employed.

> THe other ratios with duplicate values are the Solar Power Plant, Nuclear Power Plant and the Medical Clinic. 

> THIS ONLY FIXES THOSE THREE AND NOT HIGH TECH DEMAND. I have a download bundle for those fixes included.



Medical Clinic, Solar Power Plant, Nuclear Power Plant all missing jobs
----------------------------------------------


Instructions: Put HT_DemandFix.dat plugin in game (Program Files) plugins folder.


I edited the values for demand created as follows:

Medical Clinic
OLD: $ 1	$$ 6	$$$ 1
NEW: $ 2	$$ 5	$$$ 1

Solar Power Plant
OLD: $ 10	$$ 12	$$$ 10
NEW: $ 11	$$ 12	$$$ 9

Nuclear Power Plant
OLD: $ 20	$$ 20	$$$ 8
NEW: $ 22	$$ 18	$$$ 8





Thanks for using my patch! Any issues just post them on the Simtropolis Exchange download page for this.


Misc notes:

There are some other "bugs" in the game.

> The game uses a routefinder path that gets sims to go to work with the shortest distance rather than the quickest route. I have not included a fix in the but the mod which fixes it is called NAM - I decided not to include this as I wanted to just get the more simple mods included.

> Area 51 base cannot be built in the same city as Air Force base. I don't think this is actually a bug though.

> Private Schools: like the bug with Opera house. Once the student threshold inside the school radius is met (the capacity is 1000) they become overcrowded. Overcrowded schools lead to a lower education grade for the entire city, in the same way as the overcrowded opera house was known to cause.
I didn't include this fix as the patch adds a rather unrealistic slider that allows maximum capacity of 10000 and limousine travel in replacement of bus funding. I found that 1000 capacity is more realistic and you will have to add non-private schools to deal with the overflow.
