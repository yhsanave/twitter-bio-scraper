# Instructions

1. Go to the [Twitter API Playground](https://oauth-playground.glitch.me/?id=usersIdFollowing&params=%28%27id%21%27%27%7Euser.fields%21%27entities%27%7Emax_results%21%27500%27%7Epagination_token%21%27%27%29_) page and enter your user id in the `id` field. This should be a long number, not your handle/username. You can use [this site](https://www.codeofaninja.com/tools/find-twitter-id/) to get your id if you don't know it.
   
2. Hit run and grant oauth permissions to the app if prompted. The page will probably run very slow since it is rendering a lot of data, you can get it a bit faster by decreasing the `max_results` value, but you can only do 15 requests every 15 minutes so if you have too many follows, you may have to wait. You can also grab the response out of devtools if you know what that means, but you will have to reformat it later.

3. Click the + button once the response loads to copy it to the clipboard and paste it in your preferred editor. Save as a `.json` file in the `./raw/` directory. 

4. Scroll to the bottom and find the value labelled `next_token`. Paste this into the `pagination_token` field (I recommend refreshing the page to speed it up each time). 

5. Run the query again to get the next page of results and save that to a second `.json` file. 

6. Repeat steps 3-5 process until a query doesn't return a `next_token` value, at which point you have all collected all of the users you follow.

7. Run `reduce_json.py` to combine all of the data into a single json file. If you pulled the value from devtools, you may need to reformat so it looks like the [example data](#example-data) below.
   
8. Run `parse.py` to extract links from all of the bios and save them in a formatted markdown file.

---

## Example Data

```json
{
  "data": [
    {
      "url": "https://t.co/vGDjiIH5ni",
      "id": "14343311",
      "entities": {
        "url": {
          "urls": [
            {
              "start": 0,
              "end": 23,
              "url": "https://t.co/vGDjiIH5ni",
              "expanded_url": "http://www.willmcgugan.com",
              "display_url": "willmcgugan.com"
            }
          ]
        },
        "description": {
          "urls": [
            {
              "start": 17,
              "end": 40,
              "url": "https://t.co/90g34bZPn7",
              "expanded_url": "http://Textualize.io",
              "display_url": "Textualize.io"
            }
          ]
        }
      },
      "name": "Will McGugan",
      "username": "willmcgugan"
    },
    ...
  ],
  "meta": {
    "result_count": 500,
    "next_token": "...", // This is the token you put in the pagination_token field
    "previous_token": "..."
  }
}
```