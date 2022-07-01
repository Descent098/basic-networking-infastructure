from ezprez.core import *
from ezprez.components import *

# Structure of a web app
Slide("Structure of a web app", background="red")

## Traditional view
Slide("Traditional Structure", "There are two parts of an app, the front end and the back end", Image("traditional-view", "traditional-view.png"), background="red")
Slide("Front end", "This is the part people see, in a web app it's the HTML/CSS/JS that people actually see in their browsers when they go to your site", background="red")
Slide("Backend", "This is the name given to everything else. Everything that does data processing and delivering of the front-end and any data the front end needs",background="red")
Slide("Traditional Structure example", "User requests webpage --> Frontend is delievered through backend --> Frontend gets data from backend and shows user page",background="red") # Person requests service, server then processes request and responds with the frontend
Slide("The problem with this view", "The backend has way too many peices in this view, and it's responsible for multiple jobs. If you want to talk about an app saying it's a problem with the'backend' is not helpful information", background="red")

## More accuratie view
Slide("A more accurate Structure", "A more accurate structure is that there's a front end, a back end and then infastructure in-between the client and the app/site", Image("better-view", "better-view.png"), background="red") # Infastructure is not part of the backend, it is it's own system
Slide("Infastructure", "Infastructure is the name given to the peices that deliver the data to a user. It's also the name for peices that deliver the data from the frontend to the backend, but aren't involved in any of the processing.", background='red')
Slide("Why Split out infastructure?", "This makes it a bit easier to intuitively tell which peices go where, and allows you to isolate which part of an app/site you're talking about more easily, for example this means if the program running an app/site is running, but people outside the building can't see it it's an infastructure problem, not a backend problem.", background="red")
Slide("A more accurate Structure example", "User requests a webpage --> Goes through infastructure to retrieve front-end --> Front end goes back to infastructure to get data from backend --> User see's page with all content",background="red") # Person requests service, server then processes request and responds with the frontend which once it's gone through all the infastructure gets displayed
Slide("So how does infastructure work?", "For this presentation we don't care about the frontend or backend. As far as we're concerned there's a working server with all the webpages built and we're just hooking it up so people can access it outside the developers computer",background="red")

# Terminology
Slide("Let's start with some terms")
Slide("What is a browser?", "A browser lets you connect to a server over a network and then visualizes the response it recieves back (HTML/CSS/JS, images, pdf's etc.)") 
Slide("What is a network?", "A network is a collection of computers that are connected together and can communicate with one another. Generally speaking the internet is a massive network of many computers connected together") 
Slide("What is a server/host vs client?", "The server or host is the computer that is SENDING responses to the client (i.e. when you go to google, the computer that gives you the page is the server and google is the host)", "The client is whatever is RECIEVING the responses from the server (i.e. the person trying to access google and their browser)", "Technically speaking both groups do both actions, but overall the goal of the client is to recieve from the server and overall the goal of the server is to send to the client")

## URL Explanations
Slide("What is a URL?", "A URL is what you type in a browser to get a webpage, for example https://schulichignite.com/beginner it has multiple parts and follows the form:", Code("", "https://schulichignite.com/beginner\n$Protocol://$domain.$tld/$slug"), r"*Anything in angle brackets or starting with a $ is a variable")
Slide("What is a slug?", "The slug is the bit at the end, so in https://schulichignite.com/beginner the /beginner is the slug. This is used to specify what you are looking for on the server. One site can have many pages so a slug is how the server knows what to look for", "Slugs used to just be file paths, so for example you would have https://schulichignite.com/beginner.html, which the server would just look for the beginner.html file and send it")
Slide("What is a tld?", "The TLD (Top level domain) is the .com in https://schulichignite.com/beginner. The difference is that some TLD's have rules, for example .ca domains require you to provide your address and name, and the .io domain requires certain security standards etc.")
Slide("What is a protocol?", "We'll come back to this in a bit, on the web this is basically always http:// or https://, if you're loading a file it will be file://$filepath")
Slide("What is a domain?", "A domain is essentially a name you purchase. You buy a domain name (which includes A tld not all tld's), and that indicates you own it and can do what you want with it. For example schulichignite.com (this is also sometimes called a FQDN (fully qualified domain name)")


# Domain Name registrar
Slide("How does your browser know who owns a domain?", "This is where a domain name registrar comes in. You pay them to validate that you own a domaain")
Slide("Common Domain Name Registrars", "These are a dime a dozen but in Canada I would recommend either GoDaddy, webnames or namecheap (remember you have to renew your ownership or other people can take your domain)")
Slide("Great so we own the domain, but how do people talk to it?","Well they need to request a URL, and we need to give them a response")

# HTTP 
Slide("HTTP", "hyper-text transfer protocol; This is what defines how two computers structure their data to talk to each other (it's the http or https at the beginning of a URL)", background="black-blue")
Slide("HTTP Diagram", "Imagine bobby wants to get the shulich ignite beginner sessions page (https://schulichignite.com/beginner)", Image("bobby-http", "bobby-http.png"), "This whole interaction and how it works is defined by the HTTP protocol",  background="black-blue")

## Headers
Slide("HTTP Headers","HTTP requests and responses both have headers. Headers are key-value pairs that tell the client & host the details they need to interact properly", background="black-blue")
Slide("Mail analogy", "Imagine you're sending mail, you need 3 things", ["Your address", "Their Address", "The content of the letter"] ,"", "That is what HTTP needs", ["Address the communication was sent from", "Address it's going to", "The Content (text, html, image etc.)"],"", "Additionally like how you would add FRAGILE to mail to tell the post service how to handle your message, headers can also contain information about how to handle the request/response", background="black-blue")
Slide("How to examine headers in browser", "First open your browser dev tools, go to the network tab and then either refresh or navigate to a webpage", Image("view-headers","view-headers.png"),background="black-blue")

## Requests
Slide("HTTP Requests", "The first part of HTTP communication is to request a URL", background="black-blue")
Slide("HTTP Request Example", "We're going to request https://schulichignite.com/beginner",Code("","GET /beginner HTTP/1.1\nHost: schulichignite.com\nUser-Agent:... Removed for readability"), background="black-blue")
Slide("HTTP Request types (GET/HEAD)", "A GET request asks for a response that includes a header and some content, a HEAD request asks for just a header response without any content",background="black-blue") # GET
Slide("HTTP Request types (POST)", "A POST request POSTs some content to a server. This is usually done for forms to submit the data",background="black-blue") # POST
Slide("HTTP Request types (PUT)", "A PUT request tells the server to PUT whatever is being sent at the location specified. This might be used on a photo sharing service to indicate replacing a photo with a new version.",background="black-blue") # PUT
Slide("HTTP Request types (DELETE)","A DELETE request is used to ask a server to DELETE a resource (i.e. a photo)", background="black-blue") # DELETE
Slide("Other HTTP Request types", Link("This link contains more request types", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods"), background="black-blue") # DELETE
Slide("Breaking down the headers", "This won't cover everything, just the things that are useful", background="black-blue")
Slide("First line","The first line tells the browser the request type, slug, protocol and version", Code("bash", r"GET /beginner HTTP/1.1"), background="black-blue")
Slide("Host", "This tells the server & browser the domain you're trying to access", Code("","Host: schulichignite.com"), background="black-blue")
Slide("User Agent", "This tells the server information about your browser. This is used by developers often to patch compatability if a browser doesn't support a feature (usually REALLY long)", Code("","User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36 Edg/103.0.1264.37 "), background="black-blue")

## Responses

response_example = '''<pre><code class="language-html hljs xml">HTTP/1.x 200 OK
Content-Type: text/html; charset=UTF-8
Cache-Control: max-age=3600, public
Content-Encoding: gzip

&lt;title&gt; Schulich Ignite &lt;/title&gt;&lt;!--More HTML here--&gt;
</code></pre>
'''
Slide("HTTP Response", "The response is comprised of a header, and the response content (the HTML or file contents of the resource) Example", Raw(response_example),background="black-blue")
Slide("HTTP Response header example", "Like requests the response headers provide additional details. Usually about the type of content being sent and other information",Code("","HTTP/1.x 200 OK\nContent-Type: text/html; charset=UTF-8\nCache-Control: max-age=3600, public\nContent-Encoding: gzip"), background="black-blue")
Slide("Breaking down HTTP Response header", "Again this isn't everything, just things that are often useful", background="black-blue")
Slide("First line", "First line is always the response protocol, version and status code", Code("","HTTP/1.x 200 OK"), background="black-blue")
Slide("HTTP Response status codes 2xx", "These codes means everything is working as intended. Examples:",Code("","200 OK; Successful response\n201 Created; A new file was created successfully\n202 Accepted; The request has been accepted, but isn't done yet"), background="black-blue")
Slide("HTTP Response status codes 3xx", "These codes are called redirect codes. Examples:", Code("", "300 Multiple choices; Means there are a few options (like various image or file formats the browser can choose from)\n301 Moved permanantly; This request and any future requests should look to a provided URL instead of the one they requested\n302 Moved Temporarily; Temporarily go to a different provided URL, but next time check back here again"),background="black-blue")
Slide("HTTP Response status codes 4xx", "These are Client error codes (meaning you made a mistake). Examples:", Code("","400 Bad Request; You broke something, probably a syntax error or request size is too big\n403 Forbidden; You need permissions the server thinks you don't have\n404 Not found; The slug you provided has no valid response on the server\n418 I'm a teapot; :)"),  background="black-blue")
Slide("HTTP Response status codes 5xx", "These are server errors (meaning the host made a mistake)",Code("","500 Internal Server Error; Something broke, but the server won't give specifics (like a web segfault)\n502 Bad Gateway; Server couldn't get a valid response when trying to generate one from another server's data\n503 Service Unavailable; Server is borked and completely down (hopefully it's not yours)"), background="black-blue")
Slide("Other HTTP Response codes", Link("Wikipedia link", "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"), background="black-blue")
Slide("Content-Type", "This is used to tell the browser the type of info you recieved. Not everything we do is going to have an html file as a response (can have images, pdfs, file downloads etc.). This will have the file's MIME type (type of file it is) & encoding (the type of characters it supports)", Code("", "Content-Type: text/html; charset=UTF-8"), Link("List of common MIME types", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types"), Link("Common encodings", "https://unicodebook.readthedocs.io/encodings.html#:~:text=The%20three%20most%20common%20encodings,UTF%2D8%20(1996).", color="#ff0000"), background="black-blue")
Slide("Cache Control", "The cache control sets how long a page should be considered 'fresh' by the browser before asking the server to update it", Code("","Cache-Control: max-age=3600, public"), Link("Details about settings", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control"),background="black-blue")
Slide("Content Encoding", "Web pages aren't usually sent as plaintext that is human readable. They often use an encoding to save space. This header tells you which encoding is used so you know how to decode it", Code("","Content-Encoding: gzip"),Link("More details", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding"),background="black-blue")
Slide("Great, so we know about domains & HTTP let's go", "So we should be able to just connect to the domain and send HTTP requests and get responses, right?", background="black-blue")


# Domain Name System
Slide("Public IP addresses and ports", "HTTP connects to the PUBLIC IP address and port of a computer, not the domain!", "Let's say that a computer is like an apartment building. You can think of the IP address as the coordinates to the building (computer), and the port as which apartment to go to in the building (computer)", Code("","192.0. 2.146:80\n[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:443"),background="green")
Slide("How does a browser know a server's PUBLIC IP address and port based off the domain?", "The domain name registrar tells us who owns it, but once you own the domain you need to configure it. That's where DNS comes in!", background="green")
Slide("But wait, there's another server involved", "Nameservers are the in-between step where your domain name registrar tells your browser where to go to find your DNS server and records", Image("ns", "ns.png"),background="green") 
Slide("So to recap at this point", "We have made a request to a domain, we then check with the domain name registrar for the nameservers to find the DNS. Now we need to know how the DNS works", background="green")

## DNS records
Slide("DNS is made up of records", "Your domain is used for lots of things, so DNS has lots of different types of records to handle those situations. You can think of records like a contact list. It lets you look up where to communicate with a server.",Image("kieranwood-dns","kieranwood-dns.png"), background="green")
Slide("Common DNS Record types", "Here are the most common DNS records you should know about. Please note the records are listed in the following format",Code("","$record_type $domain_name $content"), "also keep in mind @ in place of domain name is self-referential (i.e. using @ for dns of schulichignite.com would be the same as typing schulichignite.com)",background="green")
Slide("Alias records (A or AAAA)", "There are two types of alias records A or AAAA, these map a domain to an IP. A records for IPV4 adresses and AAAA for IPV6", "These are the primary records used to tell the browser which server to look for to get a site", Code("","A @ 185.199.111.153\nAAAA @ 2001:0db8:85a3:0000:0000:8a2e:0370:7334"),background="green")
Slide("Canonical Name Records (CNAME)", "These are used to set a domain to another domain. For example this would allow you to have www.schulichignite.com which maps to the same content as schulichignite.com, or spark.schulichignite.com map to the content of schulich-ignite.github.io", Code("","CNAME spark schulich-ignite.github.io"),background="green")
Slide("Mail Exchanger Record (MX)", "These are records used to setup a SMTP (email) server",Code("","MX shuclichignite.com mail.domain.com"),background="green")
Slide("TXT Records", "These are just plain text, they are often used to verify to third party services (like google) that you own a domain", Code("","TXT @ $verification_code"), background="green")
Slide("NS Records", "These records tell you which nameserver is used for a domain", Code("","NS @ $nameserver_domain"),background="green")
Slide("The rest", Link("Wikipedia page of all DNS records", "https://en.wikipedia.org/wiki/List_of_DNS_record_types"), background="green")

## DNS Providors & validation
Slide("DNS providors", "Sometimes your domain name registrar will provide DNS. It is usually better to go with a dedicated DNS, I highly recommend", Link("cloudflare","https://www.cloudflare.com/", color="#eeeeeee"),background="green")
Slide("Checking DNS records", "There are some online tools:", Link("dnschecker", "https://dnschecker.org/"),"linux also includes a tool typically called dig, you can install this on windows by installing BIND", "I also wrote a python tool you can use:", Link("sws", "https://github.com/descent098/sws"), background="green")


# Putting it all together
Slide("Putting it all together", "Let's go through a full example one step at a time", background="purple")
Slide("Step 1", "Someone types https://schulichignite.com/beginner/ into their browser and hit's enter", Image("step 1", "step-1.png"),background="purple")
Slide("Step 2", "Browser pings the domain name registrar the domain was bought with and determines the nameservers", background="purple")
Slide("Step 3", "Now the browser has the nameservers, since we want the site we're looking for an A, AAAA or CNAME record (in this case it's an A record pointing to github pages)", Image("step 3", "step-3.png"), background="purple")
Slide("Step 4", "The HTTP request is then passed to the IP address and port listed", Image("step 4", "step-4.png"),background="purple")
Slide("Step 5", "The site is hosted with github pages, which recieves the request and looks for the corresponding HTML page for the /beginner slug", Image("step 4", "step-4.png"), background="purple")
Slide("Step 6", "The browser recieves an HTTP response with a 200 status code that has the content of the webpage requested (additional HTTP requests will be made for assets in the HTML file like images and external CSS files)", Image("step 6", "step-6.png"), background="purple")


# Extra stuff
Slide("Extra stuff", "Here are some extra concepts that are useful to know", background="white")

## Subdomains
Slide("Subdomains", "Along with your regular domains you can have subdomains, these allow you to have records that are controlled by the same DNS but point to different servers (i.e. https://spark.schulichignite.com/ vs https://schulichignite.com/)" ,background="white")

## SSL
Slide("We said before the protocol is called HTTP, then why do most URL's have HTTPS?", "HTTPS(ecure) is an addition to HTTP that makes it safer to use. It adds in what is called an SSL (secure socket layer) certificate (or TLS) which encrypts web traffic. Most browsers REQUIRE a valid SSL certificate in order for people to access your site.", background="white")

## CDN
Slide("CDN's", "These are servers that operate at the infastructure level, they store resources and cache them so you don't have to go to the server to retrieve them. For example if you have a CDN for all your images then when your pages load you reduce the stress on your servers because it doesn't need to handle those requests.","Having CDN versions of CSS and JS files is also very common instead of keeping all your source files on one server", background="white")

## Sockets
Slide("Ok but then how does HTTP REALLY communicate under the hood", "I'm going to cover this very broadly, essentially it relies on something called websockets. Websockets (or just sockets) allow your computer to communicate to ther computers over a network. All HTTP requests and responses get passed over sockets (as well as other protocols)", Link("Example socket-based HTTP server integrated with ezcv", "https://github.com/Descent098/ezcv-http/blob/main/socket%20testing/routes.py#L18-L118"), background="white")
Slide("Socket servers/hosts have 4 steps", "You can look into these with more detail yourself", background="white")
Slide("Set socket options", "You need to set the socket options such as what type of IP address (IPV4 or IPV6) to use, what connection type (TCP, UDP etc.) and any additional options", Link("Code example", "https://github.com/Descent098/ezcv-http/blob/main/socket%20testing/routes.py#L19-L24"), background="white")
Slide("Bind the socket", "Binding a socket means you set the INTERNAL IP address (0.0.0.0 is the easiest since it allows anything with network access to talk to it) you want to use as well as the port (80 for unencrypted and 443 for encrypted is standard)", Link("Code Example", "https://github.com/Descent098/ezcv-http/blob/main/socket%20testing/routes.py#L25"), background="white")
Slide("Ask the socket to listen", "Does what it says on the tin, it sets the server to wait for a request to come in (HTTP Requests in our case)", Link("Code example (also line 38)", "https://github.com/Descent098/ezcv-http/blob/main/socket%20testing/routes.py#L26"), background="white")
Slide("Process client request and send response", "Take in the client request, determine the content and headers you want to send back", Link("Code example", "https://github.com/Descent098/ezcv-http/blob/main/socket%20testing/routes.py#L40-L118"), background="white")

## Handy CLI tools 
Slide("Some handy tools/commands you can use", background="white")
Slide("(ifconfig/ip)/ipconfig", "Gives you the information about the LOCAL IP of your machine (for PUBLIC IP you need to google it or have it provided)", background="white")
Slide("ping", "ping can be used to check if a server is running you can use a domain or IP", Code("bash", "ping shulichignite.com\nping 8.8.8.8"),background="white")
Slide("netcat/telnet","Netcat/telnet are used for many things, but one thing both can be used for is connecting to a server and sending requests and getting responses (example is just connecting)", "linux", "nc -l port", "windows", Code("bash", "telnet hostname port"), background="white")

## Great Channel
Slide("A great channel for networking info", Link("Hussein Nasser", "https://www.youtube.com/c/HusseinNasser-software-engineering"), background="white")

# Setup the presentation
presentation_title = "Basic Networking & Infastructure"
presentation_description = "Everything you need to know to understand the steps from you typing a URL in your browser to seeing a webpage"
presentation_url = "https://kieranwood.ca/basic-networking-infastructure"
prez = Presentation(presentation_title, presentation_description, presentation_url, background="gray")

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")
