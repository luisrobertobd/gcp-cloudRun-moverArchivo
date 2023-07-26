FROM python:3.9.1

# Install nano editor just in case we need to write some file
RUN apt-get update 
RUN apt-get -y install nano 

# Install the python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files in the existing folder into /home/cuentalaboral202307/dk
WORKDIR /app
COPY . .

# Export google application credentials to have the necessary permission
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service_account.json"
ENV BUCKET="bk_lrbd_taller_001"
# Run app.py when the container launches
ENTRYPOINT ["python", "main.py"] 
