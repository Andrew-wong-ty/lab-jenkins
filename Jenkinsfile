pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                echo 'Test Step: We run testing tool like pytest here'
                '''

            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our porject'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
        stage('Scan') {
            steps {
                script {
                    def scannerHome = tool 'sonarqube'
                    withSonarQubeEnv(installationName: 'sq1') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=firstProject \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://34.174.174.113:9000 \
                            -Dsonar.token=sqp_b85f24b477b6fe4a846977882d481644b6a2dba5
                        """
                    }
                }
            }
        }

    }
}
