function sendSpreadsheetToPython() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var url = 'http://YOUR_WINDOWS_MACHINE_ADDRESS:PORT'; // Replace with your Windows machine address and the port your Python script is listening on
    
    // Fetch the desired range and values you want to send
    var range = sheet.getDataRange(); 
    var values = range.getValues();
  
    // Convert the values to a JSON string
    var payload = JSON.stringify({"data": values});
  
    // Set the options for the post request
    var options = {
        'method' : 'post',
        'contentType': 'application/json',
        'payload' : payload
    };
  
    // Send the post request to the Windows machine
    var response = UrlFetchApp.fetch(url, options);
  
    // Optionally capture and log the response content
    var content = response.getContentText();
    Logger.log(content);
}
