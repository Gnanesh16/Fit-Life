pipeline {
    agent any

    environment {
        MAVEN_HOME = '/opt/maven'  // Path to Maven installation
        JAVA_HOME = '/usr/lib/jvm/java-11-openjdk'  // Path to Java installation
        PATH = "$MAVEN_HOME/bin:$JAVA_HOME/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/fitlife-app.git'
            }
        }

        stage('Compile') {
            steps {
                script {
                    // Running the Maven clean compile command
                    sh 'mvn clean compile'
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    // Running the Maven test command
                    sh 'mvn test'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Running the Maven package command to create the artifact (JAR/WAR)
                    sh 'mvn package'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'target/*.jar', allowEmptyArchive: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage (optional for code compile job)'
            }
        }
    }

    post {
        success {
            echo 'Build and tests passed!'
        }

        failure {
            echo 'Build or tests failed!'
        }
    }
}
