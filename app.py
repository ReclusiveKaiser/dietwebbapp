import Website


from Website import create_app


app = create_app()

if __name__ == '__main__':   #Thisds means that only if we run this file not if we import this file to execute the web
    app.run(debug=True)
    #This will run the flask application and web server. The Debug = True which means everytime we change our python code it will automatically rerun the web server 
