pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'git-credentials-id' // Replace with your actual credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/malgasujith/pythonapidev.git', 
                    credentialsId: GITHUB_CREDENTIALS
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                  # Update package lists
                  sudo apt-get update
                  
                  # Install python3-venv and python3-pip if not already installed
                  sudo apt-get install -y python3-venv python3-pip
                  
                  sudo apt-get install -y libpq-dev
                  
                  # Create a virtual environment in the workspace
                  python3 -m venv venv
                  
                  # Activate the virtual environment using bash
                  bash -c "source venv/bin/activate && pip install --upgrade pip"
                  
                  # Install requirements from the correct requirements.txt file
                  bash -c "source venv/bin/activate && pip install -r oopsapidev/requirement.txt"
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                  # Activate the virtual environment and run the application using bash
                  bash -c "source venv/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"
                '''
            }
        }
    }
}
