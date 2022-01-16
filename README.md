# Google map apis HTTP Cloud Function Testing
- The function's purpose is for testing the google map `directions` api.
- This function requires `origin` and `destination` (both in `string` format) in the request JSON or DATA in order to query the directions from `origin` to `destination`. 
- It returns a JSON String with the directions guiding steps.
# Deploying HTTP Cloud Function
Auto deploying function to Google Cloud Functions by github actions after each `push` request.

# Testing the function
1. Automate test by github actions with `pytest`
2. Manual test by cUrl or Postman:

    a. cUrl:
    ```bash
        curl --header "Content-Type: application/json" \
        --request POST \
        --data '{"origin": {origin_point}, "destination": {destination_point}}' \
        https://us-central1-synthetic-cargo-314006.cloudfunctions.net/search_directions
    ```
    Example:
    ```bash
        curl --header "Content-Type: application/json" \
        --request POST \
        --data '{"origin": "Big C Thang Long, "destination": "Vincom Nguyen Chi Thanh}' \
        https://us-central1-synthetic-cargo-314006.cloudfunctions.net/search_directions
    ```

    b. Postman:

        - Open Postman web service with `https://web.postman.com`.
        - Create new HTTP Request.
        - Change type to POST request.
        - Trigger URL: `https://us-central1-synthetic-cargo-314006.cloudfunctions.net/search_directions`.
        - Click on the `Body` tab, change the body type to `raw` data with `JSON` format.
        - Input JSON: 
        ```
            {
                "origin": {origin_point},
                "destination": {destination_point}
            }
        ```
        Example:
        ```
            {
                "origin": "Big C Thang Long",
                "destination": "Vincom Nguyen Chi Thanh
            }
        ```
        - Click `Send` request to test trigger the cloud functions.
        --> Expect to receive the String with directions guiding in the Response section.