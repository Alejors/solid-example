# SOLID principles example

This is a simple project which intents to explain the advantages of coding using SOLID principles.

## Not SOLID

Inside the not-solid directory there is a simple script which works, *not-solid.py*. Has a single class which saves packages (which is expected to have an ID and a destination, eventhough it could have anything since there is no Package class describing this object) then lists them and saves them to a file.

This is NOT SOLID-based code, since this one and only class is responsible for everything, extending behavior implies opening the class itself, there are no dependency injections, no interfaces being used and therefore. Not an scalable code.

This can be run using 

>cd not-solid && python3 not-solid.py

You would expect to see the print to console of both packages, and a new file would appear inside the directory.

## SOLID

On the other hand, the SOLID directory *main.py* file does the same, but applying every principle.

### Services

Shipping class is a service which is only responsible for Adding and Listing packages. Through the implementation of a strategy it can Save its packages to a file.

### Strategies

Strategies are the different ways the interfaces are implemented. Since this project was thought to be scallable, a strategy pattern was taken and therefore the same Service can implement different strategies during its life-cycle.

#### Liskov Dependencies

There is a child strategy, which implements PackageSaver interface and extends its behavior by "sending an email" (no actual mail is sent, this would require credentials and a SMTP service at least) after the file is created. Since this is a child class, extends the behavior, but the parent class does not depend on it.

### Factory

Thinking on a webservice application we could receive a request which tells us "I need the file to be csv", or maybe "I need a pdf". Therefore the strategy need to be fabricated during runtime and not hardcoded. 
Lines inside the code like:

```
try:
  # Define a different strategy
  extension = "csv"
  ...
```

Represent what anyone would expect from ***request.body.extension*** for example. And the strategy is looked upon the extension found there.

### Entities

The definition of what should a Package's attributes be is well defined in a separate class responsible for this.


## Extending

So... Extending behavior is easy now. We need a class which saves a PDF file: go to *package_saver.py*, define PDFFileSaver and implement save_packages using a library which can write a PDF File ([py-pdf](https://github.com/py-pdf/pypdf) for example). Then just tell the factory which class to return when pdf extension is received.

```
extensions = {
  ...
  "pdf": PDFFileSaver 
}
```

## Now...Why?

Requirements get unorderly. One day a client will need to create a text file and just save it to some bucket. A couple of weeks or months later, a different client will tell you: *"I need the file to be csv formatted and sent by email"*. And some time later someone will say: *"Could it be possible to send it as a Slack message to the channel where finance people are?"*. 

This implementations could result in messy "if-else" statements in a single class script. Prompt to errors, delivering a bug-fill service which gives a terrible impreession. Therefore, begin with a solid **SOLID-based** code.