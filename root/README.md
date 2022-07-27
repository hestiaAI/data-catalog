# Data Catalog

Catalog describing data formats relevant to facilitating data exchange between many different actors in a decentralised way.

## Table of Contents



## What's inside?

This repository contains various folders containing information and templates for describing data from various sources.

There are two main folders, the `data-specific`, and the `entity-specific`.

### `data-specific`: Data descriptions for data categories

### `entity-specific`: Data descriptions for data-holding organisations

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

## Credits

Initial contributors are the [DatingPrivacy](https://dating-privacy.hestialabs.org/en/) and [other projects](https://hestialabs.org/en/projects/) supported by [HestiaLabs](https://hestialabs.org).
