pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat(script: 'python3 app.py', returnStatus: true, returnStdout: true, label: 'python')
      }
    }

    stage('artifact') {
      steps {
        echo 'success'
      }
    }

  }
}
