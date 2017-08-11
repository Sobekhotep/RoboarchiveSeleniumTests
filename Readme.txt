Chek list of Roboarchive in English
https://docs.google.com/document/d/1Y6SsGyk3UFk80Fpc6_VKX99JbXJrmOorFN4oGBMWvwo/edit?usp=sharing

Win 7 x64, browser Firefox 51.0.1 (32-bit)
 

Expected availability of the search result / absence of a search result.
 
1. Test search field - perform action, then click "Search."
 
·      Do not enter characters. Make sure results are not empty.
·      Enter the letter "a" of the Russian alphabet lower case. Make sure results are not empty.
·      Enter the letter "A" Russian alphabet upper case. Make sure results are not empty.
·      Enter the Space. Make sure results are not empty.
·      Enter the point. Make sure results are not empty.
·      Enter the @. Make sure there are no results on the page.
·      Write the first letter "a" of the English alphabet in the lower case. Make sure there are no results on the page.
·      Enter number 1. Make sure results are not empty.
·      Enter a number and a letter without a space of the Russian alphabet "1a". Make sure there are no results on the page.
·      Enter a number and a letter without a space of the English alphabet "1a". Make sure there are no results on the page.
·      Maintain two identical letters of the Russian alphabet "aa". Make sure results are not empty.
·      Write two identical letters of the English alphabet "aa". Make sure there are no results on the page.
·      Enter the word available in the database - " Уфа ". Make sure results are not empty.
·      Enter the word available in the database - " уезд ".Make sure results are not empty.
·      Enter the word available in the database - " губерния ". Make sure results are not empty.
·      Enter the word available in the database - " Оренбург ". Make sure results are not empty.
·      Enter the word available in the database - " Минск ". Make sure results are not empty.
 
 
2.       Testing the search in the НИАБ database: tick the НИАБ field, perform an "action", then click the "Search" button.
·      Do not enter characters. Make sure results are not empty.
·      Enter the first letter "a" of the Russian alphabet in lowercase. Make sure results are not empty.
·      Enter 1 letter "A" of the Russian alphabet in uppercase. Make sure results are not empty.
·      Enter the Space. Make sure results are not empty.
·      Enter the point. Make sure results are not empty.
·      Enter the special character "@". Make sure there are no results on the page.
·      Write the first letter "a" of the English alphabet in the lower case. Make sure there are no results on the page.
·      Write the first letter "A" of the English alphabet in the lower case. Make sure there are no results on the page.
·      Enter one digit "1". Make sure results are not empty.
·      Enter a number and a letter without a space "1a". Make sure there are no results on the page.
·      Enter the number and letter of the Russian alphabet with a space between them "1 a". Make sure there are no results on the page.
·      Write two identical letters of the Russian alphabet "aa". Make sure there are no results on the page.
·      Write two identical letters of the English alphabet "aa". Make sure there are no results on the page.
·      Enter the word available in the ЦГИА РБ database and absent in the НИАБ database - “Уфа”.  Make sure there are no results on the page.
·      Enter the word available in the ЦГИА РБ database and absent in the НИАБ database - "губерния ". Make sure there are no results on the page.
·      Enter the word available in the database - " уезд ". Make sure results are not empty.
·      Enter the word, which is available in the ЦГИА РБ database and is absent in the НИАБ database - “Оренбург”. Make sure there are no results on the page.
·      Enter the word available in the НИАБ database and absent in the ЦГИА РБ database - “Минск”. Make sure results are not empty.
 
3. Testing the search in the ЦГИА РБ database: tick the field of the ЦГИА РБ, perform the "action", then click the "Search" button.
 
·      Do not enter characters. Make sure results are not empty.
·      Enter 1 letter "a" of the Russian alphabet in lowercase. Make sure results are not empty.
·      Enter 1 letter "A" of the Russian alphabet in uppercase. Make sure results are not empty.
·      Enter a Space. Make sure results are not empty.
·      Enter a point. Make sure results are not empty.
·      Enter the special character "@". Make sure there are no results on the page.
·      Write the first letter "a" of the English alphabet in lowercase. Make sure there are no results on the page.
·      Write the first letter "A" of the English alphabet in lowercase. Make sure there are no results on the page.
·      Enter one digit "1". Make sure results are not empty.
·      Enter a number and a letter without a space "1a". Make sure there are no results on the page.
·      Enter the number and letter of the Russian alphabet with a space between them "1 a". Make sure results are not present.
·      Enter two identical letters of the Russian alphabet "aa". Make sure results are not empty.
·      Enter two identical letters of the English alphabet "aa". Make sure there are no results on the page.
·      Enter the word available in the ЦГИА РБ database and absent in the НИАБ database - "Уфа". Make sure results are not empty.
·      Enter the word available in the ЦГИА РБ database and absent in the НИАБ database - "губерния". Make sure results are not empty.
·      Enter the word available in the database - "уезд". Make sure results are not empty.
·      Enter the word available in the ЦГИА РБ database and absent in the НИАБ database – «Оренбург». Make sure results are not empty.
·      Enter the word available in the НИАБ database and absent in the ЦГИА РБ database - «Вилейка». Make sure there are no results on the page.
 
4.      Testing URLs for various search parameters. The URL must change after making changes to the search parameters confirmed by pressing the "Enter" button.
 
Press the button "Enter". The URL value is:
http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=&gasrb=false&niab=false&page=1&search=&todate=
 
Mark the НИАБ field with a tick, click the "Enter" button. The URL value is: http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=&gasrb=false&niab=true&page=1&search=&todate=
 
Mark the field of the ЦГИА РБ by ticking the box, press the "Enter" button. The URL value is: http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=&gasrb=true&niab=false&page=1&search=&todate=
 
Mark the " Заголовок документа " field by ticking, then press "Enter" button. The URL value is: http://roboarchive.org/search?docdescription=false&doctitle=true&emptysearch=true&fromdate=&gasrb=false&niab=false&page=1&search=&todate=
 
Mark the " Описание документа " field, click "Enter". The URL value is: http://roboarchive.org/search?docdescription=true&doctitle=false&emptysearch=true&fromdate=&gasrb=false&niab=false&page=1&search=&todate=
 
Enter  the  value  "1800"  in  the  "От"  field and the value "1900" in the "До" field of the time range, press the button "Search" (Enter). The URL value is:
 http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=1800&gasrb=false&niab=false&page=1&search=&todate=1900

Enter the value of "Уфа" in the search field, click "Search" (Enter). The URL value is: http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=&gasrb=false&niab=false&page=1&search=%D0%A3%D1%84%D0%B0&todate=
 
Enter the value of "Уфа" in the search field, tick the field ЦГИА РБ, enter the value "1800" in the field "От" and the value "1900" in the "До" field of the time range, click "Enter". Select the search page 5. The URL value is: 
http://roboarchive.org/search?docdescription=false&doctitle=false&emptysearch=true&fromdate=1800&gasrb=true&niab=false&page=5&search=%D0%A3%D1%84%D0%B0&todate=1900

