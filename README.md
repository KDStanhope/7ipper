# 7ipper
Parallel Multithreading Thing to 7zip files.

This is the barebones solution to the problem of getting the most out of high end hardware. 

Most of the programs I use day to day don't seem to take full advantage of my hardware. 
My Threadripper has 12 cores and most programs will use 1 to 4. 
My RAID drive can hit 800mb/s but I seldom use that potential. 

My solution is simply to spawn multiple processes where possible. A great example is 7zip. 
7zip doesn't appear to use all of the CPU cores despite that particular flag being switched on. 
The read/write speed also doesn't appear to be a limiting factor.

So I zip multiple file at the same time. As many files as cores. The result is about 40% quicker for TIFF files. 
I need individual 7z files too so two birds. 

This also works INCREDIBLY well for chunking up certain tasks in Global Mapper using scripting and launching multiple instances.
In the case of contour generation over a large dataset, running multiple chunks of the same dataset concurrently results in a 620% increase in speed. 
