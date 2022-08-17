Obj:

1. Login
2. Pass configurable search inputs 
3. Build search URLS
4. Get output from search URLs and derive profiles to scrape
5. Get information from profiles and structure the output
6. Save

Limitations:
  1. Code uses selenium and bs4
  2. Need manual authentication to pass security check
  3. Getting 429 error frequently (rate limiting/throttling). Have to check optimal rate on which we can scrape
  4. Files written to output
  5. Variables not taken out such as file path and counters
  6. Search args list
  7. Page counters are  fixed to 50
  8. Error handling is done in a basic way by skipping if unable to retrieve element
  9. Reusable code should be managed in better way
  10.Current speed 5 threads/ 100 profiles / 20 min  Details -->  Random 5 0 100 2022-08-17 09:42:22.379164 2022-08-17 10:02:50.289380
  11.Doesnt store data in DB yet
  
Proposed Architecture:


 Azure functions (Get URL) --  Azure EVent Hub - Azure functions (Event hubs trigger)-- Cosmos DB (parsed output) -- Cleanse -- Processed data in DB -- Analytics
                                                                                     -- BLob (compressed HTML storage)  
  Key vault (manage credentials)
Aspects to think:
1. How to use multiple logins for authentication? Also, How to determine how LinkedIn stops abuse? -- Yet to explore
2. How to determine how many search URLs to build? -- This is not necessary as URLs to scrape would be sent to event hub
3. How to determine confidence /priority of a search profile? -- To be taken at the stage of analytics once we get historical trend of profile scores
4. Explore Ways to extract profiles which match search criteria apart from search page -- ALternatives like "people you may know tag"
5. How to queue and process profiles which are to be scraped? -- We will use serverless functions like azure functions/AWS lambda.
6. How to rate limit / throttle number of profiles to scrape? -- While we have mechanisms like sleep and batching along with rate limit on azure functions side need to finalise a concrete mechanism
7. How to parallelly scrape profiles? -- Threading / azure functions
8. How to build reusable components to parse different details of parser? Any re-usable component? -- Yet to explore
9. How to decide how frequently we have to scrape a profile? - Historical analysis needed
10. How do we maintain versions of a profile? -- Cosmos DB document versioning and store latest snapshot in structured DB
11. Where can we get metadata of external information from other data providers for lookup information? -- YEt to explore
12. How thread can poll for next url when it is done with scraping of one profile? - Feedback mechanism to be implemented to queue
13. Do we need any cache while looking up for if a profile is already scanned? - Helps
14. How do we avoid duplicate scraping? As single profile can match multiple search criteria - Use lookup mentioned in point 13
15. What to do in case of error while building search URL or  scraping profiles? - Log error and move forward . Analyse trends of errors and re-inforce code to fix that
16. Right partition strategy to save page source? -- Yet to explore
17. Logging? -- Log errors and health of profiles scraped into Log analytics or other log storage
18. Right compression format to store page source? - Gzip
19. Scroll pause time and implicit wait? -- Yet to explore
20. Alternatives for selenium and beautiful soup to scrape? -- Yet to explore
21. How to rate limit based on IPs -- Yet to explore
22. How to handle 404 /429 (http error codes) -- Yet to explore
23. Trace performance of scraping -- Logging (mentioned in step 17) 
24. Trace how actively we should download a profile -- HIstorical analysis needed

EventHub —> Trigger —> Azure cosmos Db — > postgres
