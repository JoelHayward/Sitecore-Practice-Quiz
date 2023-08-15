import random
import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, question, correct_answer, other_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.answers = other_answers
        self.answers.append(correct_answer)
        random.shuffle(self.answers)

class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Sitecore Practice Quiz")
        self.master.geometry("1200x600")

        self.questions = []
        self.frame_questions = tk.Frame(master, width=600, height=600, bd=1)
        self.frame_questions.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame_scores = tk.Frame(master, width=600, height=600, bd=1)
        self.frame_scores.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.all_scores = self.load_all_scores()
        self.master_quiz_scores = self.load_master_quiz_scores()

        self.questions_pool = [
            Question("What does the abbreviation 'CDN' stand for in the context of Sitecore?", "Content Delivery Network", ["Content Development Network", "Custom Design Node", "Core Database Node"]),
    Question("What is the main purpose of Sitecore's xDB?", "Collect and connect customer data to provide a comprehensive view of the customer", ["Improve website speed", "Manage website themes", "Secure customer data"]),
    Question("Which of the following is NOT a feature of Sitecore's xDB?", "It allows you to build and deploy websites", ["It collects customer data from all channels", "It connects customer data for a comprehensive view", "It allows for personalization based on collected data"]),
    Question("What is the main function of Sitecore's Universal Tracker?", "Tracking user interactions across multiple channels", ["Improving search performance", "Managing multiple websites", "Automating marketing tasks"]),
    Question("What is the purpose of a xConnect client in Sitecore?", "It serves as an intermediary between your application and xConnect, allowing you to read, write, and search for contacts and interactions", ["It creates new websites", "It manages user permissions", "It improves website load times"]),
    Question("What is the purpose of dividing configuration files into layers in Sitecore?", "To control load order and provide better control over when files are loaded at runtime", ["To increase file size", "To improve UI", "To reduce system requirements"]),
    Question("What is the function of the Sitecore layer in Sitecore's configuration files?", "It contains configuration files for standard Sitecore components and features", ["It contains user data", "It contains security settings", "It contains network configurations"]),
    Question("What is the function of the Modules layer in Sitecore's configuration files?", "It contains configuration files for official Sitecore modules", ["It contains configuration files for Sitecore themes", "It contains configuration files for users", "It contains security settings"]),
    Question("What is the function of the Custom layer in Sitecore's configuration files?", "It contains the patch files you create in order to modify settings in the default Sitecore configuration", ["It contains user data", "It contains security settings", "It contains network configurations"]),
    Question("What is the function of the Environment layer in Sitecore's configuration files?", "It contains the patch files you create to configure Sitecore for different environments, such as QA, production, or development", ["It contains security settings", "It contains network configurations", "It contains user data"]),
    Question("In which layers are you allowed to change Sitecore settings by placing patch files?", "Custom and Environment", ["Sitecore and Modules", "Sitecore and Custom", "Modules and Environment"]),
    Question("Which layers should you not modify or add files to in Sitecore?", "Sitecore and Modules", ["Custom and Environment", "Sitecore and Custom", "Modules and Environment"]),
    Question("What is the default order of loading configuration files in Sitecore?", "Basic system files, Sitecore layer, Modules layer, Custom layer, Environment layer", ["Environment layer, Custom layer, Modules layer, Sitecore layer, Basic system files", "Modules layer, Sitecore layer, Basic system files, Custom layer, Environment layer", "Custom layer, Modules layer, Sitecore layer, Basic system files, Environment layer"]),
    Question("What is the role of the layers.config file in Sitecore?", "It defines the layers and the order in which they load at runtime", ["It defines user roles and permissions", "It manages the database connection", "It controls the website's appearance"]), Question("How can you control the sequence in which your patch files load in Sitecore?", "By adding a <loadOrder> setting to the layer", ["By renaming the files alphabetically", "By moving the files to a different folder", "By changing the file extension"]), Question("What change was made with Sitecore 9 in terms of configuration files loading?", "It introduced the ability to specify the order in which config files load", ["It introduced a new file format", "It removed the ability to load files in a specific order", "It automated the loading process"]), Question("What does a 'core role' mean in the context of Sitecore?", "It is an instance of the core Sitecore application with certain features enabled or disabled", ["It is a user role with full access to Sitecore features", "It is a basic Sitecore feature available in all versions", "It is a role assigned to the main Sitecore administrator"]), Question("How does personalization work in Sitecore?", "It displays targeted content to contacts based on their characteristics and behavior", ["It customizes the website's appearance", "It personalizes the user interface of the Sitecore application", "It allows users to personalize their accounts"]), Question("How do you set up personalization in Sitecore?", "By using the Rule Set Editor to add rules and actions to a specific component", ["By customizing the website's CSS", "By writing custom code in the backend", "By adjusting the website's settings in the control panel"]),
    Question("What is the function of the `layers.config` file in Sitecore?", "It defines the layers and the order in which they load at runtime", ["It stores user data", "It contains security settings", "It manages network configurations"]), Question("What is the purpose of Sitecore's Experience Platform (XP)?", "To create personalized experiences across all channels", ["To manage user permissions", "To improve website speed", "To build and deploy websites"]), Question("How does Sitecore's personalization feature work?", "It uses the Rule Set Editor to add rules and actions to a specific component, using these rules to display targeted, relevant content based on the characteristics and behavior of the contacts", ["It manually adjusts the website content for each user", "It changes the website layout based on user preferences", "It tracks user interactions across multiple channels"]), Question("What are the core roles in Sitecore?", "These are instances of the core Sitecore application with certain features enabled or disabled. In a fully scaled deployment, a dedicated instance performs each role", ["These are user roles with specific permissions", "These are the main modules of the Sitecore platform", "These are the main components of the Sitecore database"]), Question("What is the main benefit of using Sitecore as a CMS?", "It provides a comprehensive solution for managing content and customer experiences across multiple channels", ["It is the fastest CMS available", "It offers the best security features", "It supports the most programming languages"]), Question("What is a patch file in Sitecore?", "A file that is used to modify settings in the default Sitecore configuration", ["A file that contains security updates", "A file that is used to fix bugs in the system", "A file that is used to add new features to the system"]), Question("How can you control the sequence in which patch files load in Sitecore?", "By adding a <loadOrder> setting to the layer", ["By renaming the patch files", "By moving the patch files to a different folder", "By changing the file extensions"]), Question("In what order does Sitecore load files within a configuration layer?", "Sitecore loads the files in each subfolder in alphabetical order, with files in the root of a folder merging before files in subfolders within the folder", ["Sitecore loads the files in the order they were created", "Sitecore loads the files in reverse alphabetical order", "Sitecore loads the files randomly"]), Question("What is the main benefit of using xDB in Sitecore?", "It collects and connects customer data from multiple channels to provide a comprehensive view of each customer, enabling personalization and effective marketing", ["It speeds up the website load times", "It manages user permissions", "It secures customer data"]), Question("What does xConnect do in Sitecore?", "It serves as an intermediary between your application and xConnect, allowing you to read, write, and search for contacts and interactions", ["It manages the website themes", "It improves website load times", "It secures customer data"]),
    Question("What is the primary programming language used to develop Sitecore?", "C#", ["PHP", "Java", "Python"]),
    Question("What is the main function of the Sitecore Content Management (CM) server?", "Editing and updating content", ["Rendering web pages", "Routing and load balancing", "Database management"]),
    Question("In Sitecore, what is the role of the Content Delivery (CD) server?", "Rendering web pages", ["Editing and updating content", "Routing and load balancing", "Database management"]),
    Question("What do you call the process of creating a component in Sitecore that displays a collection of data?", "Rendering", ["Routing", "Datasource", "Indexing"]),
    Question("Which of the following is not a type of Sitecore item?", "Solution", ["Template", "Layout", "Placeholder"]),
    Question("What does the abbreviation 'xDB' stand for in Sitecore?", "Experience Database", ["Extended Database", "XML Database", "XAML Database"]),
    Question("What does the abbreviation 'SPEAK' stand for in Sitecore?", "Sitecore Process Enablement & Accelerator Kit", ["Sitecore Personalization & Engagement Acceleration Kit", "Sitecore Programming Environment & Automation Kit", "Sitecore Presentation & Editing Accelerator Kit"]),
    Question("Which Sitecore tool allows you to test and personalize content for different users?", "Experience Editor", ["Content Editor", "Workbox", "Sitecore Rocks"]),
    Question("Which Sitecore tool is used to build custom interfaces for Sitecore users?", "SPEAK", ["Content Editor", "Experience Editor", "Workbox"]),
    Question("What is the primary purpose of the Sitecore Publishing Service?", "Improving publishing performance", ["Adding new publishing targets", "Customizing publishing restrictions", "Monitoring publishing status"]),
    Question("In Sitecore, what is the function of an index?", "Improving search performance", ["Storing content data", "Managing layout settings", "Assigning security roles"]),
    Question("Which of these is not a standard Sitecore search provider?", "Bing", ["Lucene", "Solr", "Azure Search"]),
    Question("What is the main function of the Sitecore Experience Accelerator (SXA)?", "Rapid website development", ["Performance monitoring", "User interface customization", "Mobile app development"]),
    Question("What do you call the Sitecore functionality that enables you to track user interactions and personalize their experience?", "xDB", ["SXA", "SPEAK", "Solr"]),
    Question("What is the role of Sitecore Cortex in the Sitecore Experience Platform?", "Machine learning", ["Content management", "Performance monitoring", "Website development"]),
    Question("Which of the following is not a part of Sitecore's Digital Marketing System (DMS)?", "Sitecore Rocks", ["Campaign Creator", "Engagement Automation", "Email Experience Manager"]),
    Question("In Sitecore, what is the function of a placeholder?", "Defining where components can be added", ["Storing content data", "Applying styling to components", "Creating reusable components"]),
    Question("What is the primary purpose of Sitecore's Content Testing feature?", "Optimizing content through A/B testing", ["Monitoring user interactions", "Customizing the user interface", "Managing content versions"]),
    Question("Which Sitecore module provides the ability to manage multiple websites within a single Sitecore instance?", "Multisite Management", ["Experience Accelerator", "Content Testing", "Email Experience Manager"]),
    Question("What is the main advantage of using Sitecore's Email Experience Manager (EXM)?", "Creating, sending, and tracking emails within Sitecore", ["Improved email design", "Support for multiple email clients", "Enhanced security"]),
    Question("What is the primary function of the Federated Experience Manager (FXM) in Sitecore?", "Integrating external websites with Sitecore's marketing features", ["Managing user roles and permissions", "Creating and managing digital campaigns", "Optimizing website performance"]),
    Question("What is the main use of Sitecore's Web Forms for Marketers (WFFM)?", "Creating forms for data collection", ["Building custom workflows", "Automating marketing tasks", "Designing web pages"]),
    Question("What does the abbreviation 'PaaS' stand for in the context of Sitecore?", "Platform as a Service", ["Program as a Service", "Page as a Service", "Process as a Service"]),
    Question("What do you call a series of tasks that an item can pass through in Sitecore?", "Workflow", ["Workbox", "Workpath", "Workline"]),
    Question("In Sitecore, which functionality allows for the tracking of all changes made to an item?", "Versioning", ["Indexing", "Archiving", "Caching"]),
    Question("Which of the following is not a standard part of the Sitecore client interface?", "Data Manager", ["Content Editor", "Experience Editor", "Desktop"]),
    Question("Which of the following is not a type of database in Sitecore?", "Relational Database", ["Master Database", "Web Database", "Core Database"]),
    Question("What is the primary purpose of the 'master' database in Sitecore?", "Storing all versions of all items", ["Rendering web pages", "Managing user roles", "Storing configuration data"]),
    Question("What is the main function of the 'web' database in Sitecore?", "Serving content to the live website", ["Storing all versions of all items", "Managing user roles", "Storing configuration data"]),
    Question("What is the primary function of the 'core' database in Sitecore?", "Storing configuration data", ["Serving content to the live website", "Storing all versions of all items", "Managing user roles"]),
    Question("In Sitecore, what is a 'bucket' used for?", "Storing large numbers of similar items", ["Categorizing content", "Managing user permissions", "Storing configuration data"]),
    Question("What is the main use of the 'Item' class in the Sitecore API?", "Representing a piece of content", ["Managing databases", "Rendering web pages", "Tracking user interactions"]),
    Question("Which of the following is not a type of cache in Sitecore?", "Image Cache", ["HTML Cache", "Data Cache", "Item Cache"]),
    Question("What does the abbreviation 'CDN' stand for in the context of Sitecore?", "Content Delivery Network", ["Content Development Network", "Custom Design Node", "Core Database Node"]),
    Question("Which of the following is not a common task performed using the Sitecore PowerShell Extensions (SPE)?", "Creating new users", ["Bulk updating items", "Generating reports", "Automating tasks"]),
    Question("What is the main function of Sitecore's Universal Tracker?", "Tracking user interactions across multiple channels", ["Improving search performance", "Managing multiple websites", "Automating marketing tasks"]),
    Question("Where does the home item for your site is defined?", "Sitecore.config", ["Web.Config", "Layers.config", "App.config"]),
    Question("How do you retrieve your site's start item location?", "Sitecore.Context.Site.StartPath;", ["Sitecore.Context.Site.root", "Sitecore.Context.Site.PathStart", "Sitecore.Context.Site.rootPath"]),
    Question("How do you install a Sitecore package?", "Control Panel>Administration>Install a Package", ["Marketing Panel>Administration>Install a Package", "Dashboard>Administration>Install a Package", "Administration>Install a Package"]),
    Question("What's the default base template for all templates?", "Standard Template", ["Base Template", "Standard Values", "Template"]),
    Question("How can you extend the Sitecore Framework?", "Packages", ["Module", "Update Package", "Using SDK"]),
    Question("Sitecore Rocks plugin for Visual Studio can be used to perform which tasks?", "All of the above", ["Manage Packages", "Create Anti-Package for undo functionality", "Create Items", "Create Templates"]),
    Question("What is an Anti-Package?", "Helps you create a package with an option to roll back the changes", ["Helps you to import and delete the existing files", "Helps you to export the package", "None of the above"]),
    Question("The Sitecore Package Designer helps you to", "Add Items statically or dynamically", ["Sets installation options", "Remove packages", "None of the above"]),
    Question("How can you install a package in Sitecore?", "Installation Wizard", ["Sitecore Rocks", "Control Panel", "None of the above"]),
    Question("Where is the default site configuration located?", "/app_config/Sitecore.config under site", ["/app_config/Layer.config", "/config/sitecore.config under site", "Web.config under site"]),
    Question("What static class contains the information about the current HTTP request and your site installation?", "Sitecore.Context", ["Sitecore.Kernel", "Sitecore.MVC", "Sitecore.Presentation"]),
    Question("Where the Home page or start item for your site is defined in the Sitecore.config?", "Rootpath and Startitem", ["Rootpath", "Start item", "Site node"]),
    Question("How can you retrieve your site's start item location programmatically?", "String startPath = Sitecore.Context.Site.StartPath\nItem Homepage = Sitecore.Context.Database.GetItem(startPath)", ["String startPath = Sitecore.Context.Site.rootPath\nItem Homepage = Sitecore.Context.Database.GetItem(rootPath)", "String startPath = Sitecore.Context.Site.path\nItem Homepage = Sitecore.Context.Database.GetItem(path)", "String startPath = Sitecore.Context.Site.rootpath\nItem Homepage = Sitecore.Context.Database.GetItem(rootpath)"]),
    Question("What's the path of the Single website and Home Item?", "/Sitecore/Content/Home", ["/Sitecore/Home", "/Sitecore/Item/Home", "/inetpub/wwroot/Web/Home"]),
    Question("What's the recommended practices for a multisite implementation?", "All of the above", ["Creating a folder for each site", "Ensuring that each site folder has its own Home item", "Storing shared content outside of each site folder"]),
    Question("What version of Visual Studio works with the Sitecore project?", "Visual Studio 2015 or higher", ["Visual Studio 2012", "Visual Studio 2014", "Visual Studio 2015"]),
    Question("Visual Studio is the main tool to:", "All of the above", ["Configure and manage Sitecore project", "Code Layouts and renderings", "Manage configuration files"]),
    Question("Sitecore Rocks allows you to:", "All of the above", ["Create and manage site content from the Visual Studio", "Create Presentation component items and code files", "Integrate with your Visual Studio project", "Use site management tools", "Create and Install Sitecore packages"]),
    Question("Everything in Sitecore is an item", "True", ["False"]),
    Question("An item consists of:", "Fields and Field Sections", ["Data", "Content Tree"]),
    Question("The item is an addressable unit of data", "True", ["False"]),
    Question("Templates are the foundation of all content in Sitecore.", "True", ["False"]),
    Question("Templates define:", "Type of item, Determine the field sections, Determine the field names, Determine the field types", ["All of the above"]),
    Question("What does the field type determines for the field in the Content Editor and the Experience Editor?", "Editor Control", ["Options", "Value", "Security"]),
    Question("All templates inherit from the standard template", "True", ["False"]),
    Question("Modifying the base template of the template affects all items immediately", "True", ["False"]),
    Question("The Tokens in the standard values are:", "All of the above", ["$name", "$date", "$now"]),
    Question("What option overrides the Field Name in Sitecore interface?", "Title", ["Field Name", "Type", "Property"]),
    Question("Sitecore publishes items from:", "Master to Web database", ["Master to Core database", "Core to Web database", "None of the above"]),
    Question("Sitecore groups the files in layers and maps each layer to a folder in the App_Config folder", "True", ["False"]),
    Question("The Sitecore groups the files in layers and maps each layer to a folder in", "App_Config", ["Include", "wwwroot", "Sitecore"]),
    Question("What are the two types of rendering most commonly used in Sitecore", "View Rendering, Controller Rendering", ["Item Rendering", "Method Rendering", "URL Rendering"]),
    Question("Which rendering is used occasionally?", "Item Rendering", ["View Rendering", "Controller Rendering", "Method Rendering", "URL Rendering"]),
    Question("What renderings are supported only for legacy reasons?", "Method Rendering, XSLT Rendering, Url Rendering", ["All of the above"]),
    Question("Where do you create a model in Sitecore for structured data to be consumed by MVC view?", "Layout>Model", ["Template>System", "System>Model", "Sitecore>Model"]),
    Question("What steps are required for a custom route in Sitecore?", "Define a custom route, Register the custom route", ["Create a custom route", "Execute the route"]),
    Question("Areas enable you to group collections of controllers and views together to help subdivide and organize complex projects.", "True", ["False"]),
    Question("What's the recommended practice to add Sitecore libraries to your project?", "Nuget", ["Copy and paste the library from a bin folder", "Reference the dll files in the bin folder", "None of the above"]),
    Question("What are the advantages of creating a project outside of the web root folder?", "All of the above", ["Separation of Concern: between solution files and Sitecore files", "Use the same Visual Studio project when you upgrade Sitecore or create a new instance.", "Easy to backup, restore, and move project."]),
    Question("What server roles are supported in the <AppSettings> attribute of the Web.config file?", "All of the above", ["Content Delivery", "Content Management", "Processing", "Reporting", "Standalone"]),
    Question("What are three major components of the Sitecore 9 product?", "All of the above", ["Sitecore Experience Manager (XM)", "Sitecore Experience Platform (XP)", "Sitecore Experience Commerce"]),
    Question("What component-based architecture guidelines are used by Sitecore?", "Helix", ["Habitat", "Bootsrap", "Jquery", "Adaptive"]),
    Question("What are the main topics important to Helix and Modular architecture?", "All of the above", ["Dependencies", "Layers", "Modules"]),
    Question("Low coupling relies on keeping the number of dependencies between different parts down to the absolute minimum?", "True", ["False"]),
    Question("High cohesion does not rely on breaking the solution down into the right parts with logic that belong together?", "False", ["True"]),
    Question("How can you control the dependencies between modules in Sitecore?", "Use Explicit dependencies", ["Use Implicit dependencies", "Use Sitecore Rocks", "Use Content Editor"]),
    Question("The layer concept in Helix provides a structure that is extremely suitable for", "All of the above", ["Creating and maintaining solutions of any size", "Produce maintenance-friendly and clean code", "Makes the dependency flow completely clear everywhere in the solution, in Sitecore, in Visual Studio and even in the file system."]),
    Question("What layers are defined by the Sitecore Architecture Conventions?", "Project, Feature, Foundation", ["Module"]),
    Question("What's the most unstable layer in your Sitecore structure?", "Project", ["Feature", "Foundation", "Module"]),
    Question("What layer of the Sitecore Architecture Conventions stitches the features of the solution together into a cohesive solution?", "Project", ["Feature", "Foundation", "Module"]),
    Question("What layer of the Sitecore Architecture Conventions can contain page types, layout and graphical design?", "Project", ["Foundation", "Feature", "Module"]),
    Question("What layer of the Sitecore Architecture Conventions contains the concrete features of the solution?", "Feature", ["Project", "Foundation", "Module"]),
    Question("Which layer is the lowest level and most stable layer in Helix?", "Foundation", ["Project", "Feature", "Module"]),
    Question("Which layer contains the framework such as Sitecore, .Net, Bootstrap, Jquery, etc.?", "Foundation", ["Project", "Feature", "Module"]),
    Question("The concept of module is derived from:", "Component-based Architecture", ["Module-based Architecture", "Adaptive Architecture", "Helix-based Architecture"]),
    Question("Which service is responsible for processing and storing data?", "xDB", ["xConnect", "Reference Data Service", "xDB Processing"]),
    Question("Which of the following can you use to access the xDB core?", "xConnect Client API", ["Content Search API", "xDB API", "xDB Processing"]),
    Question("The client has direct access to the collection database or the search index.", "False", ["True"]),
    Question("What single endpoint name is used by the collection and Search in the development environment?", "xdb.collection", ["xdb.search", "xdb.collection search", "None of the above"]),
    Question("Where do you configure the xConnect endpoints?", "\\App_Config\\ConnectionStrings.config", ["\\App_Config\\Layers.config", "\\App_Config\\sitecore.config", "\\App_Config\\Web.config"]),
    Question("Which one of the following can help you connect to Sitecore using a Console application?", "xConnect Client API", ["xdb Service", "xdb collection service", "Content Search API"]),
    Question("Which model defines the CLR types, facets, and events?", "xConnect Collection model", ["xDB model", "Sitecore", "xConnect search"]),
    Question("The xConnect service must have a JSON representation of any model that a client application wishes to use.", "True", ["False"]),
    Question("How does the developer extend the xConnect?", "Adding Contact and Interaction facets, Adding Custom events", ["Adding items", "Adding Templates"]),
    Question("Which one of the following can help you to control the types of items that users can insert beneath an existing item?", "Using the Insert Options", ["Design Layout", "Content Editor", "Experience Editor"]),
    Question("What's the second pillar of Experience Manager?", "Content", ["Field", "Item", "Template"]),
    Question("What do you call a content instance of a template?", "Item", ["Template", "Content", "Field"]),
    Question("Where does the item store in Sitecore?", "Database", ["File System", "In an XML file", "None of the above"]),
    Question("Which database stores the edited item when you edit an item in Sitecore?", "Master", ["Web", "Core", "xDB"]),
    Question("All content is publishable when no restrictions are applied.", "True", ["False"]),
    Question("The items in Sitecore have:", "ID, Path, URL", ["All of the above"]),
    Question("Items in Sitecore do not store website content.", "False", ["True"]),
    Question("Editors do not need to lock the item before modifying it.", "False", ["True"]),
    Question("Which one the following do users need to specify when inserting an item from a template in Sitecore?", "Template Location, Item Name", ["Data Source", "Title Name"]),
    Question("Which user can create content anywhere in the tree?", "Administrators", ["Editors", "Marketers", "Users"]),
    Question("How can developers create content directly from Sitecore Explorer?", "Right-click an item > Add New Item", ["Right-click an item > Design Layout", "Right-click an item > Tasks > Add New Item", "Right-click an item > Tasks > Tools > Add New Item"]),
    Question("How can developers add multiple items at once?", "Sitecore Explorer > Right-click an item > Add New Item > Click Add on the Add new dialog box", ["Solution Explorer > Right-click an item > Add New Item > Click Add on the Add new dialog box", "Content Editor > Right-click an item > Add New Item > Click Add on the Add new dialog box", "None of the above"]),
    Question("What are the recommended practices for creating content in Sitecore?", "Place pages under the Site's Home or Start item, Set insert options, Limit the number of children, Limit the number of versions", ["All of the above"]),
    Question("The number of children that an item has and the number of versions can affect performance.", "True", ["False"]),
    Question("A regular user calls stating that he is unable to create content under the Home item. What is the possible cause of this issue?", "Insert options are not defined", ["User does not have proper rights", "User is not authenticated", "None of the above"]),
    Question("How does the language store in the content tree?", "Item", ["Template", "Data", "Information"]),
    Question("Where do you manage languages in Sitecore?", "Control Panel", ["Dashboard", "Marketing Panel", "Content Editor"]),
    Question("Each language version can have its own list of numbered versions.", "True", ["False"]),
    Question("Where can you set a friendly name for an item that can be translated?", "Display Name", ["Context Menu", "Item Name", "None of the above"]),
    Question("How does Sitecore handle an item without a Display Name?", "Name is used as a fallback", ["Generate an exception", "Hides the item", "None of the above"]),
    Question("Name and Display appear on the content item for all users.", "False", ["True"]),
    Question("The fields in Sitecore can be:", "Versioned, Shared, Unversioned", ["All of the above"]),
    Question("What version is created by default when you create a field in Sitecore?", "Versioned", ["Shared", "Unversioned", "Single Versioned"]),
    Question("Which option will allow users to create a single version of the field value for all languages?", "Shared", ["Versioned", "Unversioned", "Single Versioned"]),
    Question("Which option will allow users to create a unique version of the field value per language?", "Unversioned", ["Versioned", "Shared", "Single Versioned"]),
    Question("All fields must be versioned in Sitecore.", "False", ["True"]),
    Question("Sitecore automatically translates the labels, button text, etc. in other languages that you specify.", "False", ["True"]),
    Question("Where does Sitecore look for the language when a user clicks the URL or a link on the web page?", "The sc_lang query string parameter, The language prefix in the path in the requested URL, The language cookie associated with the context site, The default language associated with the context logical site, The DefaultLanguage setting specified in Sitecore.org", ["All of the above"]),
    Question("Why is setting the icons and creating user-friendly names important when working with the templates in Sitecore?", "It's easier for the user to identify the template for creating items.", ["To impress users", "Save space on the server", "Templates will not render without icons"]),
    Question("What's the best way to define default values and settings for items?", "Use a base template", ["Use item fields", "Use Template's standard values", "None of the above"]),
    Question("What is the recommended practice for data Architecture?", "Making good use of Template Inheritance, Using Icons and user-friendly names for templates, Using a template's Standard Values to define default values and settings for items", ["All of the above"]),
    Question("What is the recommended practice for Content Structure?", "Controlling the user experience and content tree by configuring Insert Options, Ensuring the tree structure mirrors the site structure, Limiting the child items and item versions", ["All of the above"]),
    Question("What layer(s) does the Sitecore.Services.Client framework provide on both the Server and the Client side of the Sitecore applications for the developers to use to develop data-driven applications?", "Service", ["Project", "Foundation", "Data"]),
    Question("Which Web API does the Sitecore.Services.Client use as a foundation?", "ASP.NET Web API", ["Content Search API", "xConnect Client API", "xDB API"]),
    Question("What attribute needs to be set on the controller to enable the features of the Sitecore.Services.Client framework?", "[ServicesController]", ["[ClientController]", "[APIController]", "[WebController]"]),
    Question("What two services are provided by the Sitecore.Services.Client framework?", "ItemService, EntityService", ["DataTemplateService", "ConnectService"]),
    Question("What service of Sitecore.Services.Client can be used by the developer to gain access to regular Sitecore Items?", "ItemService", ["EntityService", "DataTemplateService", "ConnetService"]),
    Question("What service of Sitecore.Services.Client can be used to gain access to business objects that you define?", "EntityService", ["ItemService", "DataTemplateService", "ConnetService"]),
    Question("What server-side classes can the client side of Sitecore applications use when using Sitecore.Services.Client?", "SPEAK components, Client-side JavaScript, Restful API directly", ["All of the above"]),
    Question("What are the two types of items in the Sitecore database?", "Definition Items, Content Items", ["Items", "Web Items", "Templates"]),
    Question("Which item defines the configuration or structure of the implementation?", "Definition Item", ["Data Items", "Content Items", "None of the above"]),
    Question("In which environment are Definition items created and managed?", "Development", ["Production", "Test", "All of the above"]),
    Question("The Definition items are managed and created in the production environment and moved as part of versioned deployments from development to test to production.", "False", ["True"]),
    Question("Which one of the following item types are Definition items?", "All items in the Core database", ["Layout and Rendering items", "Template and Field Items", "Placeholder and setting items", "Custom Field Types", "Lookup items for settings"]),
    Question("What items are managed by the editors on the website?", "Content Items", ["Definition Items", "Both a and b", "None of the above"]),
    Question("What items are owned by the Administrators and Editors in the production environment?", "Content Items", ["Definition Items", "Both a and b", "None of the above"]),
    Question("Which content item is owned by production and should never be overwritten by an item coming from the development or test environment?", "Site home page item", ["Template", "Field", "None of the above"]),
    Question("The Definition items and some content items in Sitecore are created and managed in the development environment.", "True", ["False"]),
    Question("What allows items stored in the Master or Core database to be written to disk in a text-based format and subsequently restored into a database?", "Serialization", ["Restore", "Versioning", "None of the above"]),
    Question("What tools are recommended to be used for item Serialization in Sitecore?", "TDS, Unicorn", ["Github", "Sitecore Rocks"]),
    Question("It is highly recommended to deploy business logic and items together in your deployment process.", "True", ["False"]),
    Question("What are the two tools that you can use to create and edit the content on your website?", "Content Editor, Experience Editor", ["Sitecore Editor", "Sitecore Rocks"]),
    Question("Which tool can editors use to edit and write content directly on the page?", "Experience Editor", ["Content Editor", "Sitecore Rocks", "Sitecore Editor"]),
    Question("Which tool is best for more experienced content authors who are familiar with Sitecore and the functionality that it contains?", "Content Editor", ["Sitecore Rocks", "Experience Editor", "Sitecore Editor"]),
    Question("You can edit all the items on the page using Experience Editor even if they do not belong to the selected item.", "True", ["False"]),
    Question("What is a shared layout?", "Contains the content that all versions of the page, in all languages", ["Contains a combination of the specific for the current version of the page and the content that is specified in the shared layout.", "Both a and b", "None of the above"]),
    Question("What is a final layout?", "Contains a combination of the specific for the current version of the page and the content that is specified in the shared layout.", ["Contains the content that all versions of the page, in all languages", "Both a and b", "None of the above"]),
    Question("What functionality lets you preview all your items on your website without publishing them first?", "Preview", ["Publish", "Home", "View"]),
    Question("What's the default publishing target in Sitecore?", "Web database", ["Master database", "Core database", "xDB"]),
    Question("The item can only be published if all its ancestors have been published. Which option(s) should be checked when publishing an item in Sitecore?", "Publish subitems, Publish related items", ["Both a and b", "None of the above"]),
    Question("Which option will publish everything in Sitecore?", "Republish", ["Smart Publish", "Incremental Publish", "None of the above"]),
    Question("Which option will publish all items that have changed since the last publication?", "Smart Publish", ["Incremental Publish", "Republish", "None of the above"]),
    Question("Which option will publish only items that are in the publishing queue?", "Incremental Publish", ["Smart Publish", "Republish", "None of the above"]),
    Question("How many types of versions are there in Sitecore?", "Numbered Versions, Language Versions", ["Numeric Versions", "All of the above"]),
    Question("Which one of the following creates versions of an item in the same language?", "Numbered Versions", ["Language Versions", "Numeric Versions", "All of the above"]),
    Question("Which one of the following creates a version of an item in a different language?", "Language Versions", ["Numbered Versions", "Numeric Versions", "All of the above"]),
    Question("What option will create an item that is not just a copy of the original item, but one that inherits the field values from the original item?", "Clone", ["Copy", "Duplicate", "All of the above"]),
    Question("How do you identify the template that an item is based on?", "Content area > Content tab > Quick Info > Template", ["Content area > Advanced > Quick Info > Template", "Content area > Option > Quick Info > Template", "None of the above"]),
    Question("What options can be used to run a few checks on the item to make sure that it is ready to be published?", "Markup, Field Validation", ["Check an item", "Run workflow"]),
    Question("What advanced search option can be used to locate exactly the item you are looking for in the Content tree?", "Facets, Filters", ["Search Field", "Search results", "All of the above"]),
    Question("In a Multilanguage solution, which functionality will help you to control the items or fields to reuse content from another language?", "Language Fallback", ["Multilanguage Fallback", "Both a and b", "None of the above"]),
    Question("The fallback language can be enabled on:", "Items, Fields", ["Data Types", "Home", "Content Tree"]),
    Question("Item and Field fallback on the same items should not be used at the same time.", "True", ["False"]),
    Question("Which one of the following language fallback is enabled by default on the templates that dictionary entries are based on?", "Item-level fallback", ["Field-level fallback", "Both a and b", "None of the above"]),
    Question("How can you improve the time it takes to load the Experience Editor ribbon?", "Change WebEdit.ShowNumberofLockedItemsOnButton value in Sitecore.ExperienceEditor.config to false", ["Toggle down the ribbon", "Change WebEdit.ShowNumberofLockedItemsOnButton value in Sitecore.config to false", "Change WebEdit.ShowNumberofLockedItemsOnButton value in Web.config to false"]),
    Question("What two frameworks does Sitecore support?", "MVC, Web Forms", ["JSON", "Bootstrap"]),
    Question("What is the recommended practice to reference Sitecore binaries to your project?", "Nuget", ["Copy from the Sitecore installation", "Copy from Coworker's machine", "Contact Sitecore support"]),
    Question("The best practice is to set presentation details on the standard values.", "True", ["False"]),
    Question("If the Sitecore page is displaying an error 'no layout', what could be the possible cause of this error?", "Presentation details are not set", ["Component .cshtml file is missing", "Template is not set on the item", "Template is not inherited from the base template"]),
    Question("Helix guidelines and conventions focus on architecture and mapping dependencies correctly.", "True", ["False"]),
    Question("Presentation in Sitecore is carried out by:", "Layout, Component", ["Layout", "Component", "None of the above"]),
    Question("Layout in Sitecore is:", "Scaffold of the page", ["Inner parts of the page", "Component", "Template"]),
    Question("Which property of an item stores the information that Sitecore requires to build a page response?", "Presentation Details", ["Item", "Sitecore framework", "Field"]),
    Question("Which ones form a layout in Sitecore?", ".cshtml file, Definition Item", ["Item", "Source Field", "None of the above"]),
    Question("Which field of the definition item links with the layout .cshtml file?", "Path field", ["Item field", "Model", "Source Field"]),
    Question("What Sitecore helper will you use to render field values to a page?", "Field", ["Item", "Template", "Data"]),
    Question("What rendering should only display logic?", "View Rendering", ["Controller Rendering", "Item Rendering", "Template Rendering"]),
    Question("Which one of the following is the default model used by the components in Sitecore?", "RenderingModel", ["ViewRendering", "FieldRendering", "ModelRendering"]),
    Question("The field helper will accept the following arguments:", "Field Name, Item, Set of parameters", ["Template Name, Field Name", "Content Items, Layout, parameter", "None of the above"]),
    Question("If you do not specify an item in the field helper, which one of the following will be used by default to output the content?", "Context Page Item", ["Item", "Template Item", "None of the above"]),
    Question("What action will the field helper take if the data source item is not found?", "Fall back to the context item", ["Generate an exception", "Remove the item from the view", "None of the above"]),
    Question("You must use the RenderingModel in your view rendering to access a Sitecore item.", "False", ["True"]),
    Question("The Sitecore field helper can be used to render content from items, and the content can also be edited in the Experience Editor.", "True", ["False"]),
    Question("What parameter value can be set in the Sitecore Field helper to make the content read-only?", "new {DisableWebEdit=true}", ["new {EnableWebEdit=false}", "new {WebEdit=false}", "new {DisableEdit=true}"]),
    Question("What parameter value can be set in the Sitecore Field Helper to set the width and height of an image?", "mw, mh", ["Width, height", "Width, length", "All of the above"]),
    Question("The source fields in Sitecore are used to:", "Limit the set of items that can be used", ["Pull data from the database", "Make it difficult for the user to change the values", "All of the above"]),
    Question("What templates define data types in Sitecore?", "Data Templates", ["Standard Template", "Base Template", "None of the above"]),
    Question("What template defines the base template for most data templates?", "Standard Template", ["Data Templates", "Base Template", "None of the above"]),
    Question("What field values are defined by the standard template?", "None", ["Standard values", "Default values", "Items"]),
    Question("The standard template inherits from a number of base templates defined under the /sitecore/templates/System/Templates/Sections item. Each of these base templates defines a single section of the standard template.", "True", ["False"]),
    Question("The names of fields in the standard template begin with:", "Two underscores", ["One underscore", "string", "Three underscores"]),
    Question("What field types can be rendered directly in Sitecore?", "Text: Single-line, Multi-line, Rich text, Number, Integer, Date: Date, DateTime, Link: General Link, General Link with Search, Image: Image", ["Reference another item: Droplink, Grouped Droplink, Droptree", "Multiple References: Treelist, TreelistEx, Multilist, Checklist, Multilist with Search", "Boolean: Check box"]),
    Question("What field types cannot be rendered directly in Sitecore?", "Reference another item: Droplink, Grouped Droplink, Droptree, Multiple References: Treelist, TreelistEx, Multilist, Checklist, Multilist with Search, Boolean: Check box", ["Text: Single-line, Multi-line, Rich text, Number, Integer", "Date: Date, DateTime", "Image: Image"]),
    Question("What class types can be used for fields that cannot be rendered directly?", "ReferenceField, MultilistField, CheckboxField", ["Text, Date, Image", "BooleanField, LinkField", "All of the above"]),
    Question("What's the namespace for field class types: ReferenceField, MultiListField, CheckboxField", "Sitecore.Data.Fields", ["Sitecore.Data", "Sitecore.Data.Items", "None of the above"]),
    Question("What are the parameters of EditFrame()?", "DataSource, Buttons, Title, Tooltip, CssClass, Parameters", ["None of the above"]),
    Question("How can developers allow content authors to edit complex fields such as Multilist, Checkbox, and Treelist fields using the Experience Editor?", "Field Editor", ["Item Editor", "Template Editor", "All of the above"]),
    Question("What is an Edit Frame?", "A region of the page that reacts to clicking by showing a toolbar", ["A component on that page to display item values", "A view of an image displayed within a page", "None of the above"]),
    Question("Which one of the following will help a developer add a button to any toolbar to display a field editor?", "Edit Frame button", ["Complex item", "Render item", "Edit Item button"]),
    Question("What is the most significant feature of the Sitecore system when designing the user experience in Sitecore?", "Dynamic layout engine", ["Static layout engine", "Data Templates", "All of the above"]),
    Question("How should a partial view be prefixed in Sitecore?", "Underscore", ["CamelCase", "User-friendly names", "All of the above"]),
    Question("How do you register a View Rendering with Sitecore?", "Create a View Rendering definition item, Point to the path of the .cshtml file", ["Create a Controller rendering definition item, Reference the Controller and Controller Action view by name", "All of the above"]),
    Question("How do you register a Controller Rendering with Sitecore?", "Create a Controller rendering definition item, Reference the Controller and Controller Action view by name", ["Create a View Rendering definition item, Point to the path of the .cshtml file", "All of the above"]),
    Question("Placeholders are added to the markup in code and are identified with a unique placeholder key.", "True", ["False"]),
    Question("What are the advantages of using dynamic binding in Sitecore?", "New page types can be assembled from existing components, Changes to a page structure do not require a developer, Supports content reuse, Supports Sitecore's personalization and testing features", ["All of the above"]),
    Question("What binding should be used when adding Header and Footer to the layout?", "Both a and b", ["Static", "Dynamic", "None of the above"]),
    Question("When should you use static binding in Sitecore?", "Component always needs to be present on a layout or component", ["Do not have time to code", "Both a and b", "None of the above"]),
    Question("What binding should a developer use if a user wants to edit the component using the Experience editor?", "Dynamic", ["Static", "Adaptive", "All of the above"]),
    Question("Where do authors add, remove, move, and configure components?", "Experience Editor", ["Content Editor", "Both a and b", "None of the above"]),
    Question("If the Allowed Controls are not defined in the Placeholder settings, then the content users will be able to:", "Add all controls to the placeholder", ["Cannot add any controls to the placeholders", "Will not be able to use placeholders", "None of the above"]),
    Question("The placeholder settings can:", "Make placeholders selectable in the Experience Editor, Are used to restrict components", ["Both a and b", "None of the above"]),
    Question("The items in the placeholder are called:", "Definition Items", ["Templates", "Items", "Information"]),
    Question("Presentation details are set on a template's standard values but can be overridden on the item.", "True", ["False"]),
    Question("What does Sitecore create when you override presentation details on the item?", "Layout Delta", ["Layout Details", "Presentation Details", "Template for the item"]),
    Question("What happens when you create the regular placeholder multiple times on the page?", "Same content appears on both placeholder definitions with the same key", ["It creates different content in each placeholder", "It creates a unique key for each placeholder", "All of the above"]),
    Question("How can you make sure that each placeholder on the page has a unique key?", "Create dynamic placeholders using @Html.Sitecore().DynamicPlaceholder('Key')", ["Create static placeholders using @Html.Sitecore().Placeholder('Key')", "Change the Unique item in placeholder settings", "None of the above"]),
    Question("What can you do to create more flexible components on the page?", "Create dynamic placeholders", ["Create static placeholders", "Use view rendering", "All of the above"]),
    Question("Which standard field is a shared field where you specify the common layout for all languages and versions of the item?", "_Renderings", ["_Final Renderings", "_Item Renderings", "_Shared_Renderings"]),
    Question("Which standard field is a shared field where you specify individual layouts for languages and versions of items?", "_Final Renderings", ["_Renderings", "_Item Renderings", "_Shared_Renderings"]),
    Question("How are layouts stored in the fields?", "XML", ["HTML", "JSON", "Javascript"]),
    Question("How does the final presentation get created in Sitecore?", "The contents of _Renderings and _Final Rendering fields are merged ('Patched')", ["XML in _rendering field finalized", "When XML in the _Final Renderings finalized", "None of the above"]),
    Question("Which one of the following maps the item to the current URL?", "RenderingContext.Current.ContextItem", ["RenderingContext.Current.Rendering.item", "RenderingContext.Current.URL", "None of the above"]),
    Question("Which one of the following will help you to easily display contents from an item other than the context item?", "RenderingContext.Current.Rendering.item", ["RenderingContext.Current.ContextItem", "RenderingContext.Current.URL", "None of the above"]),
    Question("How can we prevent authors from selecting the wrong type of data source for the component?", "Set the Datasource Location", ["Set the Template Location", "Set Insert Options", "None of the above"]),
    Question("Where do you set up the Data Source location for a component?", "Component Toolbar > More > Edit Experience Editor Option", ["View > Advanced > Edit Experience Editor Option", "Home > Advanced > Edit Experience Editor Option", "Component Toolbar > More > Advanced > Edit Experience Editor Option"]),
    Question("How can we restrict authors to use a specific item type?", "Set the Datasource Template", ["Set the Template Location", "Set Insert Options", "None of the above"]),
    Question("What are the advantages of using the Datasource template?", "Restricts users to a specific item type, Allows content creation of that item type", ["No free-form text input", "Prevent errors", "Control Input", "Improve the user experience"]),
    Question("The Datasource Template cannot be configured with or without a Datasource location.", "False", ["True"]),
    Question("When the Datasource Template is set without the Datasource location, the authors can see the entire content tree but are only allowed to select the specific item type for that component.", "True", ["False"]),
    Question("The component parameters are stored as:", "Key-value pairs", ["XML", "HTML", "None of the above"]),
    Question("Which one of the following will allow developers to access the parameters of the component programmatically?", "@Model.Rendering.Parameters['CssClass']", ["@RenderingContext.Current.Rendering.Parameters['ButtonText']", "Both a and b", "None of the above"]),
    Question("How can developers help authors choose the correct component parameter values?", "Use fields", ["Key-value pair", "Both a and b", "None of the above"]),
    Question("What are the advantages of using Rendering Parameter templates?", "No free-form text input, Prevent errors, Control Input, Improve the user experience", ["All of the above"]),
    Question("How many parameter templates are allowed on a component?", "One", ["Two", "Three", "Unlimited"]),
    Question("Compatible Rendering is a component definition item that enables users to replace the one component with another.", "True", ["False"]),
    Question("Where else do you specify the components so they can be swapped in the Experience editor?", "Placeholder's Allowed Controls field", ["Template fields", "Control Panel", "Configuration Items"]),
    Question("How to handle redirects with Sitecore?", "Third-party modules, Custom code overriding the LinksManager and ItemSolver, IIS redirects", ["All of the above"]),
    Question("What's the benefit of using Wildcard items in Sitecore?", "Allows you to work with dynamic URLs, It matches any request, It ensures the URL is dynamic", ["All of the above"]),
    Question("What methods can be used to navigate the tree?", ".Parent(), .GetChildren(), .Axes.GetAncestors(), .Axes.GetDescendants()", ["All of the above"]),
    Question("Developers should use ContentSearch for the best performance in Sitecore.", "True", ["False"]),
    Question("You should use 'var' in a foreach loop with the ChildList.", "False", ["True"]),
    Question("What should you use instead of 'var' in a foreach loop with the ChildList?", "Sitecore.Data.Items.Item", ["Sitecore.Data.Items.Context", "Site.Data.items.Item", "None of the above"]),
    Question("LINQ is useful in Sitecore for:", "Filtering small collections of items", ["Setting up configuration", "Reviews items", "None of the above"]),
    Question("Sitecore sorts subitems alphabetically by default.", "True", ["False"]),
    Question("When you use LINQ to sort items, what needs to be done to improve performance?", "Instruct the GetChildren method not to sort items", ["Execute query right away", "Instruct Sitecore.Context not to execute the query", "None of the above"]),
    Question("What happens if you edit directly on the Web database?", "Changes are lost after a publish", ["The developers can no longer work", "Sitecore support will contact you", "Edited content automatically moves to Core database"]),
    Question("When you edit an item, how do you ensure that your changes are made on the Master database only?", "Point to the Master data using the following statement Var masterDB = Sitecore.Configuration.Factory.GetDatabase('master')", ["Change the database from the Sitecore Desktop view", "Change the database from the Sitecore Rocks plugin", "All of the above"]),
    Question("Anonymous visitors have permissions to create items in Sitecore.", "True", ["False"]),
    Question("How do you run code as another user in Sitecore?", "Sitecore.SecurityModel.SecurityDisabler(), Sitecore.Security.Accounts.UserSwitcher('usersID')", ["Sitecore.Context.Account.Switch('userid');", "None of the above"]),
    Question("What are the steps to edit content programmatically?", "Ensure you have the required permissions, Retrieve the item, Invoke the Editing.BeginEdit() method, Change the field values, Invoke the Editing.EndEdit() method", ["All of the above"]),
    Question("Which one of the following can you use when you need an endpoint to access and manipulate data remotely?", "Sitecore.Services.Client", ["Sitecore.Services.EndPoint", "Sitecore.Services.Context", "Sitecore.Services.DB"]),
    Question("Where can developers find JavaScript libraries?", "\\Sitecore\\shell\\client\\Services\\Assets\\lib", ["\\Sitecore\\shell\\configure\\Assets", "\\Sitecore\\shell\\Configure\\lib", "None of the above"]),
    Question("The Search Facets are calculated after the search.", "True", ["False"]),
    Question("Administrators can add facets for other fields/properties.", "True", ["False"]),
    Question("The search interface operations allow you to:", "Remove search results, Run bulk operations over all the search results, Format search results", ["None of the above"]),
    Question("All fields are indexed by default in Sitecore.", "False", ["True"]),
    Question("What are the benefits of using Item buckets in Sitecore?", "Reduce the number of children per item, Hide folder structure and content from Editor's view, Allow editors to search the content by bringing the search interface to the forefront", ["All of the above"]),
    Question("Where do you adjust the item bucket settings in Sitecore?", "/Sitecore/System/Settings/Buckets/Item Buckets Settings", ["/Home/System/Settings/Buckets/Item Buckets Settings", "/Content/System/Settings/Buckets/Item Buckets Settings", "/Dashboard/Control Panel/Settings/Buckets/Item Buckets Settings"]),
    Question("What API is used by the Search UI and Sitecore Buckets?", "ContentSearch API", ["ItemSearch Web API", "ContentSearch Web API", "Search Web API"]),
    Question("List two libraries that developers need to construct a search in Sitecore?", "Sitecore.ContentSearch, Sitecore.ContentSearch.Linq", ["Sitecore.Context.Item", "Both a and b", "None of the above"]),
    Question("What LINQ IQueryable methods are not supported in Sitecore?", "GroupBy, Aggregate, Sum", ["All of the above"]),
    Question("Which one of the following LINQ IQueryable methods are supported in Sitecore?", "Where, Contains, Any, All, OrderBy", ["GroupBy", "All of the above except a"]),
    Question("Why is it not recommended to use Axes.GetDescendants to retrieve a large number of items?", "Performance Issue", ["Less code", "Sitecore does not support", "Infrastructure cannot handle the query"]),
    Question("Which one of the following are the official Sitecore documentations?", "Dev.sitecore.net, Doc.sitecore.net, Sdn.sitecore.net, Kb.sitecore.net, Youtube.com/user/mastersitecore, Helix.sitecore.net", ["All of the above"]),
    Question("Which one of the following are the community-driven sources?", "Community.sitecore.net, Feeds.sitecore.net, Marketplace.sitecore.net, Sitecore.community.github.io", ["All of the above"]),
    Question("Which one of the releases adds significant functionality to a product?", "Feature Release", ["Service Pack", "Update", "All of the above"]),
    Question("Sitecore will not provide individual customers with a hotfix or patch to resolve a single issue or a small number of issues in a Sitecore product.", "False", ["True"]),
    Question("How long will Sitecore support the Mainstream Support Phase?", "3 years", ["1 year", "2 years", "Forever"]),
    Question("Which tool will you use to analyze the log files?", "Log Analyzer", ["Event Viewer", "Sitecore Log Viewer", "Microsoft Word"]),
    Question("The self-test diagnostics can be run using:", "Sitecore Diagnostics Toolset", ["Sitecore Control Panel", "Windows System settings", "Sitecore Log Settings"]),
    Question("You must supply the license ID when you open a ticket with Sitecore.", "True", ["False"]),
    Question("What needs to be attached before submitting the ticket to Sitecore Support?", "Relevant Configuration Files, Recent Log files, Screenshots of UI, errors, and related files, Exceptions as plain text documents", ["All of the above"]),
    Question("What tool can be used to generate a support package for Sitecore support?", "Support Package Generator", ["Zip application", "Sitecore Tool Generator", "All of the above"])
            # Add your questions here...
        ]

        self.answer_buttons = []

        self.question_label = tk.Label(self.frame_questions, text="", wraplength=500)
        self.score_label = tk.Label(self.frame_scores, text="Score: 0 / 0")
        self.top_score_label = tk.Label(self.frame_scores, text=self.format_top_scores())
        self.average_score_label = tk.Label(self.frame_scores, text=self.calculate_average_score())
        self.master_quiz_button = tk.Button(self.frame_scores, text="Start Master Quiz", padx=10, pady=10, command=self.start_master_quiz)

        self.question_label.pack()
        self.score_label.pack(anchor="w")
        self.top_score_label.pack(anchor="w")
        self.average_score_label.pack(anchor="w")
        self.master_quiz_button.pack(anchor="w")

    def start_master_quiz(self):
        self.questions = self.questions_pool.copy()
        self.start_quiz()

    def start_quiz(self):
        self.current_question = 0
        self.score = 0
        if len(self.questions_pool) > 50:
            self.questions = random.sample(self.questions_pool, 50)
        else:
            self.questions = self.questions_pool.copy()
        random.shuffle(self.questions)
        self.show_question()
        self.score_label['text'] = "Score: 0 / 0"
        self.update_average_score_label()


    def show_question(self):
        for button in self.answer_buttons:
            button.destroy()
        self.answer_buttons.clear()

        question = self.questions[self.current_question]
        question_number = self.current_question + 1
        self.question_label['text'] = f"Question {question_number}: {question.question}"

        for answer in question.answers:
            button = tk.Button(
                self.frame_questions,  # Change the parent to frame_questions
                text=answer,
                width=60,
                wraplength=380,
                command=lambda ans=answer: self.check_answer(ans)
            )
            button.pack(pady=5)
            self.answer_buttons.append(button)

    def check_answer(self, selected_answer):
        question = self.questions[self.current_question]
        if selected_answer == question.correct_answer:
            self.score += 1
        self.current_question += 1
        self.score_label['text'] = f"Score: {self.score} / {self.current_question}"

        correct_answer = question.correct_answer
        messagebox.showinfo("Answer", f"The correct answer is: {correct_answer}")

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        percentage = (self.score / len(self.questions)) * 100
        message = f"You've completed the quiz with a score of {self.score} out of {len(self.questions)}\n" \
                  f"Percentage: {percentage:.2f}%"
        messagebox.showinfo("Quiz Finished", message)
        self.show_restart_prompt()

    def calculate_average_score(self):
        if self.all_scores:
            average_score = sum(self.all_scores) / len(self.all_scores)
            return f"Average Score: {average_score:.2f}%"
        else:
            return "Average Score: N/A"

    def format_top_scores(self):
        if self.all_scores:
            highest_score = max(self.all_scores)
            return f"Top Score: {highest_score:.2f}%"
        else:
            return "Top Score: None"

    def save_all_scores(self):
        with open("all_scores.txt", "w") as file:
            for score in self.all_scores:
                file.write(f"{score}\n")

    def load_all_scores(self):
        try:
            with open("all_scores.txt", "r") as file:
                return [float(line.strip()) for line in file]
        except FileNotFoundError:
            return []

    def show_restart_prompt(self):
        restart = messagebox.askyesno("Restart Quiz", "Do you want to restart the quiz?")
        if restart:
            self.restart_quiz()
        else:
            self.quit_quiz()

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_question()
        self.score_label['text'] = "Score: 0 / 0"
        self.update_average_score_label()  # Update the average score label

    def quit_quiz(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit the quiz?"):
            self.master.quit()

    def update_average_score_label(self):
        self.average_score_label['text'] = self.calculate_average_score()

    def save_master_quiz_scores(self):
        with open("master_quiz_scores.txt", "w") as file:
            for score in self.master_quiz_scores:
                file.write(f"{score}\n")

    def load_master_quiz_scores(self):
        try:
            with open("master_quiz_scores.txt", "r") as file:
                return [float(line.strip()) for line in file]
        except FileNotFoundError:
            return []

root = tk.Tk()
quiz = Quiz(root)
quiz.start_quiz()  # Start the regular quiz by default
root.mainloop()
