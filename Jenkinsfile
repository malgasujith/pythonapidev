pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh '''#!/bin/bash
# Define workspace directory
workspaceDir="${WORKSPACE}"

# Echo workspace directory for debugging
echo "Workspace Directory: ${workspaceDir}"

# Navigate to workspace directory
cd "${workspaceDir}"

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the FastAPI application using uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
'''
      }
    }

    stage('artifact') {
      steps {
        echo 'success'
      }
    }

  }
}