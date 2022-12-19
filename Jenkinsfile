@Library('caelum@refs/tags/v0.12.0') _

pipeline {
    agent {
        docker {
            image '169.254.149.20:6001/arch_python_git_baw:v1.45.0'
        }
    }
    stages{
        stage('setup'){
            steps{script{baw.setup()}}
        }
        stage('test'){
            failFast true
            parallel{
                stage('doc'){
                    steps{
                        script{baw.doctest()}
                    }
                }
                stage('fast'){
                    steps{
                        script{baw.fast(2)}
                    }
                }
            }
        }
        stage('all'){
            steps{
                script{baw.all(2)}
            }
        }
        stage('quality'){
            failFast true
            parallel{
                stage('lint'){
                    steps{
                        script{baw.lint()}
                    }
                }
                stage('format'){
                    steps{
                        script{baw.format()}
                    }
                }
            }
        }
        stage('release'){
            steps{
                script{publish.release()}
            }
        }
    }
}
