pipeline {
    agent any

    environment {
        PYTHON_HOME = '/usr/bin/python3'  // Path to Python installation
        VIRTUALENV_DIR = 'venv'           // Path for virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Gnanesh16/Fit-Life'  // Replace with your repo URL
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create and activate the virtual environment
                    sh 'python3 -m venv $VIRTUALENV_DIR'
                    sh './$VIRTUALENV_DIR/bin/pip install --upgrade pip'
                    sh './$VIRTUALENV_DIR/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests
                    sh './$VIRTUALENV_DIR/bin/python -m unittest discover'
                }
            }
        }

        stage('Package as Executable') {
            steps {
                script {
                    // Package the app as an executable using PyInstaller
                    sh './$VIRTUALENV_DIR/bin/pyinstaller --onefile app.py --name fitlife-app'
                }
            }
        }

        stage('Archive Executable') {
            steps {
                archiveArtifacts artifacts: 'dist/fitlife-app', allowEmptyArchive: false
            }
        }
    }

    post {
        success {
            echo 'Packaging successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
