import requests

def JFrog():
    url = 'http://54.153.123.248:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    filepath ='/home/ubuntu/Devops/Java_app_3.0-main/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    user_name = 'admin'
    password = 'Admin@123'
    
    with open(filepath, 'rb') as file:
        response = requests.put(url, auth=(user_name, password), data=file)

    if response.status_code == 201:
        print("Successfully Uploaded to JFrog")
    else:
        print(f"Something went wrong. Status code: {response.status_code}")

JFrog()
