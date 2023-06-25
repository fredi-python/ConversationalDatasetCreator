<?php
// Get the JSONL data from the request body
$jsonData = file_get_contents('php://input');

// Generate a unique file name
$fileName = 'conversational_data_' . uniqid() . '.jsonl';

// Specify the path to save the file
$filePath = 'path/to/save/' . $fileName;

// Save the JSONL data to the file
if (file_put_contents($filePath, $jsonData) !== false) {
    http_response_code(200);
} else {
    http_response_code(500);
}
?>

