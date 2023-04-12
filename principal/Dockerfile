# Use a Tomcat image as the base
FROM tomcat:latest

# Copy the JSP files to the webapps directory in the container
COPY portal/ /usr/local/tomcat/webapps/ROOT

# Expose port 8080 for HTTP traffic
EXPOSE 8080

# Start Tomcat when the container starts
CMD ["catalina.sh", "run"]