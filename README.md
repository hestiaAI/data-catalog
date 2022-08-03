# Data Catalog

Catalog describing data formats relevant to facilitating data exchange between many different actors in a decentralised way.

* [Available data](#available-data)
* [What's inside?](#what-s-inside-)
  * [data-specific: Data descriptions for data categories](#-data-specific---data-descriptions-for-data-categories)
  * [entity-specific: Data descriptions for data-holding organisations](#-entity-specific---data-descriptions-for-data-holding-organisations)
* [Collaboration](#collaboration)
* [Credits](#credits)

---

## Available data

 * [data-specific](./data-specific)
 * [entity-specific](./entity-specific)
     * [Business](./entity-specific/Business)
     * [Communication](./entity-specific/Communication)
       * [WhatsApp](./entity-specific/Communication/WhatsApp)
     * [Dating](./entity-specific/Dating)
       * [AdopteUnMec](./entity-specific/Dating/AdopteUnMec)
       * [Bumble](./entity-specific/Dating/Bumble)
       * [Grindr](./entity-specific/Dating/Grindr)
       * [happn](./entity-specific/Dating/happn)
       * [HER](./entity-specific/Dating/HER)
       * [Parship](./entity-specific/Dating/Parship)
       * [ROMEO](./entity-specific/Dating/ROMEO)
       * [Tinder](./entity-specific/Dating/Tinder)
     * [Educational](./entity-specific/Educational)
     * [Entertainment](./entity-specific/Entertainment)
       * [BookBeat](./entity-specific/Entertainment/BookBeat)
       * [Netflix](./entity-specific/Entertainment/Netflix)
       * [Spotify](./entity-specific/Entertainment/Spotify)
       * [YouTube](./entity-specific/Entertainment/YouTube)
     * [Gaming](./entity-specific/Gaming)
     * [Lifestyle](./entity-specific/Lifestyle)
     * [Medical](./entity-specific/Medical)
     * [Misc](./entity-specific/Misc)
       * [TrackerControl](./entity-specific/Misc/TrackerControl)
     * [Social](./entity-specific/Social)
       * [Facebook](./entity-specific/Social/Facebook)
       * [Instagram](./entity-specific/Social/Instagram)
       * [LinkedIn](./entity-specific/Social/LinkedIn)
       * [TikTok](./entity-specific/Social/TikTok)
       * [Twitter](./entity-specific/Social/Twitter)
     * [Travel](./entity-specific/Travel)
       * [Uber](./entity-specific/Travel/Uber)
     * [Utility](./entity-specific/Utility)
         * [Amazon](./entity-specific/Utility/Amazon)
         * [Apple](./entity-specific/Utility/Apple)
         * [GitHub](./entity-specific/Utility/GitHub)
         * [Google](./entity-specific/Utility/Google)

---

## What's inside?

This repository contains various folders containing information and templates for describing data from various sources.

There are two main folders, the `data-specific`, and the `entity-specific`.

### data-specific: Data descriptions for data categories

TODO

### entity-specific: Data descriptions for data-holding organisations

An entity is defined as a data-holding organisation, to which a [Subject Access Requests](https://wiki.personaldata.io/wiki/Subject_Access_Request) can be made. This directory thus contains information about the formats of files received through Subject Access Requests, along with models and example data.

Entities are classified under different categories:
* **Gaming**: Description.
* **Business**: Description.
* **Educational**: Description.
* **Lifestyle**: Description.
* **Entertainment**: Description.
* **Utility**: Description.
* **Travel**: Description.
* **Communication**: Description.
* **Medical**: Description.
* **Social**: Description.
* **Dating**: Description.
* **Misc**: Description.

Of course, new categories can be created at the discretion of the contributors.

Each entity will have each own folder, containing:
* A `README.md` file that should contain a description of the entity, a description of the scripts, and a description of the templates.
* A `inputs` sub-folder that should contain synthetic data sources, mirroring an export from the entity.
* A `scripts` sub-folder which should contain the various scripts, notebooks, etc., used to create the templates.
* A `models` sub-folder which sould contain the various templates created, with a corresponding extension name.
* Whatever useful information (e.g., other models, other descriptions, links, ...).

In particular, a description of how to make a query for its data will usually be present.

For instance, the files [Happn/data/all-data/users/uuid.json](https://github.com/hestiaAI/data-catalog/blob/main/SAR/Happn/data/all-data/users/uuid.json) and [Happn/data/all-data/relationships/uuid.json](https://github.com/hestiaAI/data-catalog/blob/main/SAR/Happn/data/all-data/relationships/uuid.json) show in a privacy-preserving way how dating app [Happn](https://www.happn.com/en/) structures information about its users and relationships respectively. It contains no revealing information about the individual who contributed those files.

Those files are generated through a semi-automated process, which is constantly improving. 

## Collaboration

We are looking for collaborations in the academic and education areas, or even more generally civil society. Feel free to contact us at contact @ hestia.ai.

## Credits

Initial contributors are the [DatingPrivacy](https://dating-privacy.hestialabs.org/en/) , [The Eyeballs](https://eyeballs.hestialabs.org/en/) and [other projects](https://hestialabs.org/en/projects/) supported by [HestiaLabs](https://hestialabs.org).
