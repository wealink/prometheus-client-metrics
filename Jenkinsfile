pipeline {
    agent {
        node {
            label 'tech'
        }
    }
    environment {
        REGISTRY_HOST = "tezign.com:5000"
        DOCKER_IMAGE = "client_metrics"
        //APP_NAME = "client_metrics"
    }
    //parameters {
        //choice(name:'K8S_NAMESPACE',choices:'env5\nenv6',description:'k8s的namespace名称')
        //string(name: 'GIT_TAG', defaultValue: 'master', description: 'GIT_TAG名称')
    //}
    stages {
        stage('image') {
            steps {
                sh "docker build -t ${REGISTRY_HOST}/${DOCKER_IMAGE}:${params.GIT_TAG}_${BUILD_ID} ."
                sh "docker push ${REGISTRY_HOST}/${DOCKER_IMAGE}:${params.GIT_TAG}_${BUILD_ID}"
            }
        }
        stage('deploy'){
            steps {
                sh "docker rm -vf ${DOCKER_IMAGE}"
                sh "docker run -d -p 8081:8080 --restart always --name ${DOCKER_IMAGE} ${REGISTRY_HOST}/${DOCKER_IMAGE}:${params.GIT_TAG}_${BUILD_ID}"
            }
        }
    }
}