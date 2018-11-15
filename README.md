# iBot-Framework
An intelligence logistics framework

What’s iBot Framework?
Bot Framework is a playground where all the activity, function and interactions take place. It’s like a sandbox universe which has some governing rules that its constituents and every existing entity inside follow.

Naturally bot framework consist of all bots. You can imagine Bots as matters and rules as forces in this framework… And contexts as energies in the form of relevance factors among bots.

Bots are basically virtual agent. They each have some cognition which operates on memory function and by building awareness from it. To differentiate their function, each bot has a flavour. In bot framework there are 2 types of bots,

There are two types of bots possible in bot framework…

1. Databot
2. Metabot
you can think Databot as Atom and Metabot as Molecule…

Databots:
Databots are the smallest entity and identify with single piece of information. They learn and store all their past interactions in their memory and build their awareness around it. They also understand their function. They have Interfaces interact with other bots as well as input and output interfaces to be used with graph systems.

Metabots:
They identify with collection of bots nesting to carry out specific functions. They too learn and store all their past interactions in their memory and build awareness. They also understand their function. They too have Interfaces but they also have children interfaces from collection bots inside, they too have input and output interfaces to be used with graph systems.

Bots Memory and Awareness Functions
Memory function is a part of bots cognition. Each bot have their own memory space, bots sense any change in their state. There are primarily 2 types detection mechanism. Temporal, Contextual but there can be more custom form of awareness like Relational. And these detection pattern collected over time is called awareness. These awarenesses differ in function from each other but can also work together to improve it own own function. For example Contextual awareness could ask temporal awareness to review and build certain type of context for itself or improve some of its existing context…

Awareness in bots:

Temporal Awareness:
This awareness is at its core a function of time, it generates timestamps on certain triggering event then pushes these timestamps into temporal awareness of each bots. Triggering event could be anything, default triggers are when some function is called and all bots involved in those function will receive a timestamp of same value. You can also add any manual event as trigger. Thinking engine can also trigger this in background. These timestamps are collected over time for each bot, the awareness size can be customized for each bot. So for example, Bot A winks at Bot B then both bots will receive time same timestamp file containing the time wink interaction took place.

Contextual Awareness:
This awareness works in higher abstraction that finds a meaningful structure among bots and their functions. There could be all kinds of context. Context can be built manually or generated automatically. Temporal awareness can also be used to define and build useful context. You can also build simple queries then define the resulting bots in some contexts. So for example Sam was discussing on Artificial Intelligence with a colleague and he remembered about Michael who is an expert in AI. So Michael is contextually linked with AI in Sam’s contextual awareness. This could be expanded or restricted in size as deemed useful.

Other Awarenesses:
In theory you can have any type of custom awareness assigned to your bot cognitive model. There’s no restriction on algorithms however any awareness algorithm that optimizes the system will naturally be more valuable. You can have special case awareness which is only applicable to certain function. For example you can have a Relational awareness in a project management system Metabot. You can have frequency awareness that triggers when someone makes a specific request. However in most cases you will chose contextual awareness instead, except in very specific cases that need to deploy special algorithm that contextual awareness isn’t fit for. More examples would be evidence based, language based, predictive awarenesses.

<img src="https://github.com/meta-machine/iBot-Framework/blob/master/iBots.png" />

#Uses Command line interface Click https://click.palletsprojects.com/en/7.x/

#Commands

#create databot command. databot will ask input type. 

>>create databot firstname
    define input type.
>>text
    databot "firstname" is created

>>create databot lastname
    define input type.
>>text
    databot "firstname" is created


>>create databot dob
    define input type.
>>date
    databot "dob" is created


>>create databot phone
    define input type.
>>number
    databot "phone" is created

>>create databot email
    define input type.
>>text
    databot "email" is created    

#create metabot command.

>>create metabot person
    metabot "person" is created

>>list databots
    [firstname], [lastname], [dob], [phone], [email]

>>list bots
    [firstname], [lastname], [dob], [phone], [email], [person]




#Defining relations.
{
    >>define relation person.has    #1
        new relation "has" added to person.
    >>add firstname person.has      #2
    >>add lastname person.has       #3
    >>add dob person.has            #4
    >>add phone person.has          #5
    >>add email person.has          #6

    #operation
    #1. This command defines a new relation, basically creates a directory called "has" inside person->awareness->relational
    #2. adds firstname bot #ref inside person->awareness->relational->has, also adds "_has" directory inside firstname->awareness->relational and adds person metabot #ref index.
    #3 .. #6. similar as #2

    #note: everytime a relation is added between 2 entities. if primary entity relation is "has" then secondary entity will have "_has". 
}


#Defining context
{
    >>define context person.basicInfo           #1
        new context basicInfo added to person.
    >>add firstname person.basicInfo            #2
    >>add lastname person.basicInfo             #3
    >>add dob person.basicInfo                  #4

    #operation
    #1. This command defines a new context, basically creates a directory called "basicInfo" inside person->awareness->contextual
    #2 #4. adds directory basicInfo to these bots contextual awareness, these bots share context and have same bot #ref index. 
}

#Defining another context
{
    >>define context person.contactInfo         #1
        new context contactInfo added to person.
    >>add phone person.contactInfo              #2
    >>add email person.contactInfo              #3

    #operation
    #1. New context, contactInfo in contextual awareness of person Metabot
    #2 #3. adds directory contactInfo to these bots contextual awareness, these bots share context and have same bot #ref index. 
}

#fetches all the context for person Metabot
>>list context person
    2 contexts found.
    "basicInfo", "contactInfo"

#fetches bots from context person.basicInfo
>>list bots person.basicInfo
    3 bots with same context
    firstname, lastname, dob

#fetching works same for other bots with shared context eg.
>>list bots firstname.basicInfo
    3 bots with same context
    lastname, dob, person




>>list bots person.context.*
    6 bots found with same context
    firstname, lastname, dob, phone, email


>>person>>list relations
    1 relations found with 4 bots
    has>firstname
    has>lastname
    has>dob
    has>phone

//Nested commands for bot
>>select person
>>person>>list relations
>>person>>list context
>>person>>list bots in relation.*
>>person>>list bots in relation.has
>>person>>list bots in context.*
>>person>>list bots in context.basicInfo


