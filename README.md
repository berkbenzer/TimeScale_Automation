Retention policies may expire because there are too many reads from the timescale database. This automation was made because the failure of retention policies to 
work increases the disk usage on the system.
The general approach is to implement a Python program that recognizes when the application has been restarted.
As a first step, information that the application was closed was received and checked with the Rundeck job.
In the second step, the Python program was run for the case in which the application was closed and the retention policies were triggered.
I haven't added the final version of the Python code yet, but it can be viewed in terms of general logic.
