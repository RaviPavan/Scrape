Obj:

1. Login
2. Pass configurable search inputs 
3. Build search URLS
4. Get output from search URLs and derive profiles to scrape
5. Get information from profiles and structure the output
6. Save

Limitations:
  Code uses selenium and bs4
  Need manual authentication to pass security check
  Getting 429 error frequently (rate limiting/throttling). Have to check optimal rate on which we can scrape
  Files written to output
  Variables not taken out such as file path and counters
  Search args list
  Page counters are  fixed to 50
  
Proposed Architecture:
 Azure functions (Get URL) --  Azure EVent Hub - Azure functions (Event hubs trigger)-- Cosmos DB (parsed output) -- Cleanse -- Processed data in DB -- Analytics
                                                                                     -- BLob (compressed HTML storage)  
  Key vault (manage credentials)
Aspects to think:
1. How to use multiple logins for authentication? Also, How to determine how LinkedIn stops abuse?
2. How to determine how many search URLs to build?
3. How to determine confidence /priority of a search profile?
4. Explore Ways to extract profiles which match search criteria apart from search page
5. How to queue and process profiles which are to be scraped?
6. How to rate limit / throttle number of profiles to scrape?
7. How to parallelly scrape profiles?
8. How to build reusable components to parse different details of parser? Any re-usable component?
9. How to decide how frequently we have to scrape a profile?
10. How do we maintain versions of a profile?
11. Where can we get metadata of external information from other data providers for lookup information?
12. How thread can poll for next url when it is done with scraping of one profile?
13. Do we need any cache while looking up for if a profile is already scanned?
14. How do we avoid duplicate scraping? As single profile can match multiple search criteria 
15. What to do in case of error while building search URL or  scraping profiles?
16. Right partition strategy to save page source?
17. Logging?
18. Right compression format to store page source?
19. Scroll pause time and implicit wait?
20. Alternatives for selenium and beautiful soup to scrape?
21. How to rate limit based on IPs
22. How to handle 404 /429 (http error codes)

EventHub —> Trigger —> Azure cosmos Db — > postgres
