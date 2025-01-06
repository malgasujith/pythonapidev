pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat(script: 'python3 your_script.py', returnStatus: true, returnStdout: true, label: 'python')
      }
    }

    stage('artifact') {
      steps {
        echo 'success'
      }
    }

  }
}