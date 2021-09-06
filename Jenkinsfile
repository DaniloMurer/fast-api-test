pipeline {

    agent any

    stages {

        stage('Deploy') {
            environment {
                REMOTE_DIR = "/app/apps/fast-api-test"
                SOURCE_FILES = "**/*.py, Dockerfile, docker-compose.yml"
            }
            steps {
                echo "Deploying Security-Alert"
                sshPublisher(
                    continueOnError: false,
                    failOnError: true,
                    publishers: [
                        sshPublisherDesc (
                            configName: "administrator@danilojakob.ch",
                            verbose: true,
                            transfers: [
                                sshTransfer (
                                    execCommand: "if [ -d ${REMOTE_DIR} ]; then " +
                                                    "cd ${REMOTE_DIR} && " +
                                                    "rm -rf *" +
                                                    "; fi \n"
                                ),
                                sshTransfer (
                                    sourceFiles: env.SOURCE_FILES,
                                    remoteDirectory: env.REMOTE_DIR,
                                    execCommand: "sudo docker-compose -f /app/apps/fast-api-test/docker-compose.yml up -d --build"
                                )
                            ]
                        )
                    ]    
                )
            }
        }
    }

}