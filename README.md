# Jenkins Pipeline

This Jenkins Pipeline will run on a Docker agent and periodically check for updates from the SCM.

## Stages

1. **Build Stage**: In this stage, the dependencies listed in the "requirements.txt" file will be installed to meet the project's requirements.
2. **Test Stage**: In this stage, the "checkStatus.py" file will be executed to perform testing processes.
3. **Deploy Stage**: In this stage, the deployment processes of the project will be performed.
