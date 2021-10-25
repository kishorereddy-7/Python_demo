pipeline {
    agent any 
    stages { 
        stage("Hello") { 
            steps { 
                echo 'Hello World' 
            } 
        } 
        stage("Unit Test") {
            steps {
                sh "python unit_test.py"
            }
        }
        
    }
} 
