# Twitter data format

Sample of the Twitter data format. The archive contains over 50 files. To keep things manageable, files of similar concepts are grouped in one ShEx file, on a semi-arbitrary basis.

Code such as 
```
  {
    "niDeviceResponse" : {
      "messagingDevice" : {
        "deviceType" : "Full",
```
is described as featuring a "type" and "subtype" field with values "niDeviceResponse" and "messagingDevice", respectively.

## ShEx files and corresponding JSON files
* account: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/account.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Faccount.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * account-creation-ip.js
  * account-suspension.js
  * account-timezone.js
  * account.js
  * ageinfo.js
  * email-address-change.js
  * phone-number.js
  * profile.js
  * screen-name-change.js
  * verified.js
* activity: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/activity.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Factivity.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * like.js
  * moment.js
  * protected-history.js
  * saved-search.js
  * tweet.js
  * user-link-clicks.js
* ads: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/ads.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fads.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * ad-engagements.js
  * ad-impressions.js
  * ad-mobile-conversions-attributed.js
  * ad-mobile-conversions-unattributed.js
  * ad-online-conversions-attributed.js
  * ad-online-conversions-unattributed.js
* devices: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/devices.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fdevices.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * connected-application.js
  * device-token.js
  * ip-audit.js
  * ni-devices.js
* direct_message: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/direct_message.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fdirect_message.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * direct-message-group-headers.js
  * direct-message-headers.js
  * direct-message-mute.js
  * direct-messages-group.js
  * direct-messages.js
* periscope: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/periscope.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fperiscope.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * periscope-account-information.js
  * periscope-ban-information.js
  * periscope-broadcast-metadata.js
  * periscope-comments-made-by-user.js
  * periscope-expired-broadcasts.js
  * periscope-followers.js
  * periscope-profile-description.js
* personalisation: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/personalisation.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fpersonalisation.shex&schemaFormat=ShExC&schemaEngine=ShEx)
* user_interactions: [ShEx](https://github.com/hestiaAI/data-catalog/blob/main/shex/twitter/user_interactions.shex) — [Visualisation](http://rdfshape.herokuapp.com/schemaInfo?schemaURL=https%3A%2F%2Fraw.githubusercontent.com%2FhestiaAI%2Fdata-catalog%2Fmain%2Fshex%2Ftwitter%2Fuser_interactions.shex&schemaFormat=ShExC&schemaEngine=ShEx)
  * block.js
  * contact.js
  * follower.js
  * following.js
  * mute.js

## Todo
* lists
  * lists-created.js
  * lists-member.js
  * lists-subscribed.js
* fleet
  * fleet-mute.js
  * fleet.js
* birdwatch
  * birdwatch-note-rating.js
  * birdwatch-note.js


## JSON files (57)

```
   account-creation-ip.js
   account-suspension.js                    # EMPTY
   account-timezone.js
   account.js
   ad-engagements.js
   ad-impressions.js
   ad-mobile-conversions-attributed.js
   ad-mobile-conversions-unattributed.js    # EMPTY
   ad-online-conversions-attributed.js      # EMPTY
   ad-online-conversions-unattributed.js    # EMPTY
   ageinfo.js                               # EMPTY
   app.js                                   # EMPTY
   birdwatch-note-rating.js                 # EMPTY
   birdwatch-note.js                        # EMPTY
   block.js
branch-links.js
   connected-application.js
   contact.js
   device-token.js
   direct-message-group-headers.js
   direct-message-headers.js
   direct-message-mute.js
   direct-messages-group.js
   direct-messages.js
   email-address-change.js
   fleet-mute.js
   fleet.js
   follower.js
   following.js
   ip-audit.js
   like.js
   lists-created.js
   lists-member.js
   lists-subscribed.js
manifest.js                        # EMPTY
   moment.js
   mute.js
   ni-devices.js
   periscope-account-information.js
   periscope-ban-information.js                  # EMPTY
   periscope-broadcast-metadata.js               # EMPTY
   periscope-comments-made-by-user.js            # EMPTY
   periscope-expired-broadcasts.js               # EMPTY
   periscope-followers.js                        # EMPTY
   periscope-profile-description.js
   personalization.js
   phone-number.js
   profile.js
   protected-history.js
reply-prompt.js                        # EMPTY
   saved-search.js
   screen-name-change.js
spaces-metadata.js                        # EMPTY
sso.js                        # EMPTY
  tweet.js
  user-link-clicks.js
  verified.js
```

