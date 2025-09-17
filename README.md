Cyclic Notifier

The aim of the project is to remind you to do eye exercises.

To run notifier in as a Bash script, add the following CronJob:
```bash
*/20 * * * * <ABSOLUTE PATH TO YOUR BASH SCRIPT> >> <ABSOLUTE PATH TO YOUR LOG FILE> 2>&1
```
