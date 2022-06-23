## Twitter

### `data/account-creation-ip.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | N/A | What IP was used to create that account. |
| `$[*]` | dict | None | None |
| `$[*].accountCreationIp` | dict | None | None |
| `$[*].accountCreationIp.accountId` | str | https://schema.org/identifier | Unique account ID for that user. |
| `$[*].accountCreationIp.userCreationIp` | str | https://github.com/hestiaAI/Argonodes/wiki/General:IPv4 | Unique account ID for that user. |

### `data/account-suspension.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/account-timezone.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | N/A | N/A |
| `$[*]` | dict | None | None |
| `$[*].accountTimezone` | dict | None | None |
| `$[*].accountTimezone.accountId` | str | https://schema.org/identifier | Unique account ID for that user. |
| `$[*].accountTimezone.timeZone` | str | https://schema.org/scheduleTimezone | Timezone used when creating the account. |

### `data/account.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | N/A | N/A |
| `$[*]` | dict | None | None |
| `$[*].account` | dict | None | None |
| `$[*].account.email` | str | N/A | Email linked to that account. |
| `$[*].account.createdVia` | str | N/A | Platform used to create that account. |
| `$[*].account.username` | str | N/A | Current username for that account. |
| `$[*].account.accountId` | str | https://schema.org/identifier | Unique account ID for that user. |
| `$[*].account.createdAt` | str | N/A | Timestamp for the creation of that account. |
| `$[*].account.accountDisplayName` | str | N/A | Current display name for that account. |

### `data/ad-engagements.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].ad` | dict | None | None |
| `$[*].ad.adsUserData` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements` | list | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*]` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.deviceInfo` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.deviceInfo.osType` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.deviceInfo.deviceId` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.displayLocation` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.tweetId` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.tweetText` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.urls` | list | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.urls[*]` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.mediaUrls` | list | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTweetInfo.mediaUrls[*]` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.advertiserInfo` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.advertiserInfo.advertiserName` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.advertiserInfo.screenName` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.matchedTargetingCriteria` | list | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.matchedTargetingCriteria[*]` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.matchedTargetingCriteria[*].targetingType` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.matchedTargetingCriteria[*].targetingValue` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.impressionTime` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTrendInfo` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTrendInfo.trendId` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTrendInfo.name` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].impressionAttributes.promotedTrendInfo.description` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].engagementAttributes` | list | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].engagementAttributes[*]` | dict | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].engagementAttributes[*].engagementTime` | str | None | None |
| `$[*].ad.adsUserData.adEngagements.engagements[*].engagementAttributes[*].engagementType` | str | None | None |

### `data/ad-impressions.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].ad` | dict | None | None |
| `$[*].ad.adsUserData` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions` | list | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*]` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].deviceInfo` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].deviceInfo.osType` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].deviceInfo.deviceId` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].displayLocation` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].advertiserInfo` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].advertiserInfo.advertiserName` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].advertiserInfo.screenName` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].matchedTargetingCriteria` | list | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].matchedTargetingCriteria[*]` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].matchedTargetingCriteria[*].targetingType` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].matchedTargetingCriteria[*].targetingValue` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].impressionTime` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.tweetId` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.tweetText` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.urls` | list | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.urls[*]` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.mediaUrls` | list | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTweetInfo.mediaUrls[*]` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTrendInfo` | dict | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTrendInfo.trendId` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTrendInfo.name` | str | None | None |
| `$[*].ad.adsUserData.adImpressions.impressions[*].promotedTrendInfo.description` | str | None | None |

### `data/ad-mobile-conversions-attributed.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/ad-mobile-conversions-unattributed.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/ad-online-conversions-attributed.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/ad-online-conversions-unattributed.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/ageinfo.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].ageMeta` | dict | None | None |
| `$[*].ageMeta.ageInfo` | dict | None | None |
| `$[*].ageMeta.ageInfo.age` | list | None | None |
| `$[*].ageMeta.ageInfo.age[*]` | str | None | None |
| `$[*].ageMeta.ageInfo.birthDate` | str | None | None |

### `data/app.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/birdwatch-note-rating.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/birdwatch-note.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/block.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].blocking` | dict | None | None |
| `$[*].blocking.accountId` | str | None | None |
| `$[*].blocking.userLink` | str | None | None |

### `data/branch-links.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/community-tweet.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/connected-application.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].connectedApplication` | dict | None | None |
| `$[*].connectedApplication.organization` | dict | None | None |
| `$[*].connectedApplication.organization.name` | str | None | None |
| `$[*].connectedApplication.organization.url` | str | None | None |
| `$[*].connectedApplication.organization.privacyPolicyUrl` | str | None | None |
| `$[*].connectedApplication.organization.termsAndConditionsUrl` | str | None | None |
| `$[*].connectedApplication.name` | str | None | None |
| `$[*].connectedApplication.description` | str | None | None |
| `$[*].connectedApplication.permissions` | list | None | None |
| `$[*].connectedApplication.permissions[*]` | str | None | None |
| `$[*].connectedApplication.approvedAt` | str | None | None |
| `$[*].connectedApplication.id` | str | None | None |

### `data/contact.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/device-token.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].deviceToken` | dict | None | None |
| `$[*].deviceToken.clientApplicationId` | str | None | None |
| `$[*].deviceToken.token` | str | None | None |
| `$[*].deviceToken.createdAt` | str | None | None |
| `$[*].deviceToken.lastSeenAt` | str | None | None |
| `$[*].deviceToken.clientApplicationName` | str | None | None |

### `data/direct-message-group-headers.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].dmConversation` | dict | None | None |
| `$[*].dmConversation.conversationId` | str | None | None |
| `$[*].dmConversation.messages` | list | None | None |
| `$[*].dmConversation.messages[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].participantsLeave` | dict | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.userIds` | list | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.userIds[*]` | str | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation` | dict | None | None |
| `$[*].dmConversation.messages[*].joinConversation.initiatingUserId` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation.participantsSnapshot` | list | None | None |
| `$[*].dmConversation.messages[*].joinConversation.participantsSnapshot[*]` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation.createdAt` | str | None | None |

### `data/direct-message-headers.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].dmConversation` | dict | None | None |
| `$[*].dmConversation.conversationId` | str | None | None |
| `$[*].dmConversation.messages` | list | None | None |
| `$[*].dmConversation.messages[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.recipientId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.recipientId` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.createdAt` | str | None | None |

### `data/direct-message-mute.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/direct-messages-group.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].dmConversation` | dict | None | None |
| `$[*].dmConversation.conversationId` | str | None | None |
| `$[*].dmConversation.messages` | list | None | None |
| `$[*].dmConversation.messages[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].participantsLeave` | dict | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.userIds` | list | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.userIds[*]` | str | None | None |
| `$[*].dmConversation.messages[*].participantsLeave.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].url` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].expanded` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].display` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.text` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.mediaUrls` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation` | dict | None | None |
| `$[*].dmConversation.messages[*].joinConversation.initiatingUserId` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation.participantsSnapshot` | list | None | None |
| `$[*].dmConversation.messages[*].joinConversation.participantsSnapshot[*]` | str | None | None |
| `$[*].dmConversation.messages[*].joinConversation.createdAt` | str | None | None |

### `data/direct-messages.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].dmConversation` | dict | None | None |
| `$[*].dmConversation.conversationId` | str | None | None |
| `$[*].dmConversation.messages` | list | None | None |
| `$[*].dmConversation.messages[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.recipientId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions[*].senderId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions[*].reactionKey` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions[*].eventId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.reactions[*].createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*]` | dict | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].url` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].expanded` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.urls[*].display` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.text` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.mediaUrls` | list | None | None |
| `$[*].dmConversation.messages[*].messageCreate.mediaUrls[*]` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].messageCreate.createdAt` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate` | dict | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.recipientId` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.urls` | list | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.text` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.mediaUrls` | list | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.senderId` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.id` | str | None | None |
| `$[*].dmConversation.messages[*].welcomeMessageCreate.createdAt` | str | None | None |

### `data/email-address-change.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].emailAddressChange` | dict | None | None |
| `$[*].emailAddressChange.accountId` | str | None | None |
| `$[*].emailAddressChange.emailChange` | dict | None | None |
| `$[*].emailAddressChange.emailChange.changedAt` | str | None | None |
| `$[*].emailAddressChange.emailChange.changedTo` | str | None | None |
| `$[*].emailAddressChange.emailChange.changedFrom` | str | None | None |

### `data/follower.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].follower` | dict | None | None |
| `$[*].follower.accountId` | str | None | None |
| `$[*].follower.userLink` | str | None | None |

### `data/following.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].following` | dict | None | None |
| `$[*].following.accountId` | str | None | None |
| `$[*].following.userLink` | str | None | None |

### `data/ip-audit.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].ipAudit` | dict | None | None |
| `$[*].ipAudit.accountId` | str | None | None |
| `$[*].ipAudit.createdAt` | str | None | None |
| `$[*].ipAudit.loginIp` | str | None | None |

### `data/like.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].like` | dict | None | None |
| `$[*].like.tweetId` | str | None | None |
| `$[*].like.fullText` | str | None | None |
| `$[*].like.expandedUrl` | str | None | None |

### `data/lists-created.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/lists-member.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].userListInfo` | dict | None | None |
| `$[*].userListInfo.url` | str | None | None |

### `data/lists-subscribed.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].userListInfo` | dict | None | None |
| `$[*].userListInfo.url` | str | None | None |

### `data/manifest.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$.userInfo` | dict | None | None |
| `$.userInfo.accountId` | str | None | None |
| `$.userInfo.userName` | str | None | None |
| `$.userInfo.displayName` | str | None | None |
| `$.archiveInfo` | dict | None | None |
| `$.archiveInfo.sizeBytes` | str | None | None |
| `$.archiveInfo.generationDate` | str | None | None |
| `$.archiveInfo.isPartialArchive` | bool | None | None |
| `$.archiveInfo.maxPartSizeBytes` | str | None | None |
| `$.readmeInfo` | dict | None | None |
| `$.readmeInfo.fileName` | str | None | None |
| `$.readmeInfo.directory` | str | None | None |
| `$.readmeInfo.name` | str | None | None |
| `$.dataTypes` | dict | None | None |
| `$.dataTypes.account` | dict | None | None |
| `$.dataTypes.account.files` | list | None | None |
| `$.dataTypes.account.files[*]` | dict | None | None |
| `$.dataTypes.account.files[*].fileName` | str | None | None |
| `$.dataTypes.account.files[*].globalName` | str | None | None |
| `$.dataTypes.account.files[*].count` | str | None | None |
| `$.dataTypes.accountCreationIp` | dict | None | None |
| `$.dataTypes.accountCreationIp.files` | list | None | None |
| `$.dataTypes.accountCreationIp.files[*]` | dict | None | None |
| `$.dataTypes.accountCreationIp.files[*].fileName` | str | None | None |
| `$.dataTypes.accountCreationIp.files[*].globalName` | str | None | None |
| `$.dataTypes.accountCreationIp.files[*].count` | str | None | None |
| `$.dataTypes.accountSuspension` | dict | None | None |
| `$.dataTypes.accountSuspension.files` | list | None | None |
| `$.dataTypes.accountSuspension.files[*]` | dict | None | None |
| `$.dataTypes.accountSuspension.files[*].fileName` | str | None | None |
| `$.dataTypes.accountSuspension.files[*].globalName` | str | None | None |
| `$.dataTypes.accountSuspension.files[*].count` | str | None | None |
| `$.dataTypes.accountTimezone` | dict | None | None |
| `$.dataTypes.accountTimezone.files` | list | None | None |
| `$.dataTypes.accountTimezone.files[*]` | dict | None | None |
| `$.dataTypes.accountTimezone.files[*].fileName` | str | None | None |
| `$.dataTypes.accountTimezone.files[*].globalName` | str | None | None |
| `$.dataTypes.accountTimezone.files[*].count` | str | None | None |
| `$.dataTypes.adEngagements` | dict | None | None |
| `$.dataTypes.adEngagements.files` | list | None | None |
| `$.dataTypes.adEngagements.files[*]` | dict | None | None |
| `$.dataTypes.adEngagements.files[*].fileName` | str | None | None |
| `$.dataTypes.adEngagements.files[*].globalName` | str | None | None |
| `$.dataTypes.adEngagements.files[*].count` | str | None | None |
| `$.dataTypes.adImpressions` | dict | None | None |
| `$.dataTypes.adImpressions.files` | list | None | None |
| `$.dataTypes.adImpressions.files[*]` | dict | None | None |
| `$.dataTypes.adImpressions.files[*].fileName` | str | None | None |
| `$.dataTypes.adImpressions.files[*].globalName` | str | None | None |
| `$.dataTypes.adImpressions.files[*].count` | str | None | None |
| `$.dataTypes.adMobileConversionsAttributed` | dict | None | None |
| `$.dataTypes.adMobileConversionsAttributed.files` | list | None | None |
| `$.dataTypes.adMobileConversionsAttributed.files[*]` | dict | None | None |
| `$.dataTypes.adMobileConversionsAttributed.files[*].fileName` | str | None | None |
| `$.dataTypes.adMobileConversionsAttributed.files[*].globalName` | str | None | None |
| `$.dataTypes.adMobileConversionsAttributed.files[*].count` | str | None | None |
| `$.dataTypes.adMobileConversionsUnattributed` | dict | None | None |
| `$.dataTypes.adMobileConversionsUnattributed.files` | list | None | None |
| `$.dataTypes.adMobileConversionsUnattributed.files[*]` | dict | None | None |
| `$.dataTypes.adMobileConversionsUnattributed.files[*].fileName` | str | None | None |
| `$.dataTypes.adMobileConversionsUnattributed.files[*].globalName` | str | None | None |
| `$.dataTypes.adMobileConversionsUnattributed.files[*].count` | str | None | None |
| `$.dataTypes.adOnlineConversionsAttributed` | dict | None | None |
| `$.dataTypes.adOnlineConversionsAttributed.files` | list | None | None |
| `$.dataTypes.adOnlineConversionsAttributed.files[*]` | dict | None | None |
| `$.dataTypes.adOnlineConversionsAttributed.files[*].fileName` | str | None | None |
| `$.dataTypes.adOnlineConversionsAttributed.files[*].globalName` | str | None | None |
| `$.dataTypes.adOnlineConversionsAttributed.files[*].count` | str | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed` | dict | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed.files` | list | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed.files[*]` | dict | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed.files[*].fileName` | str | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed.files[*].globalName` | str | None | None |
| `$.dataTypes.adOnlineConversionsUnattributed.files[*].count` | str | None | None |
| `$.dataTypes.ageinfo` | dict | None | None |
| `$.dataTypes.ageinfo.files` | list | None | None |
| `$.dataTypes.ageinfo.files[*]` | dict | None | None |
| `$.dataTypes.ageinfo.files[*].fileName` | str | None | None |
| `$.dataTypes.ageinfo.files[*].globalName` | str | None | None |
| `$.dataTypes.ageinfo.files[*].count` | str | None | None |
| `$.dataTypes.app` | dict | None | None |
| `$.dataTypes.app.files` | list | None | None |
| `$.dataTypes.app.files[*]` | dict | None | None |
| `$.dataTypes.app.files[*].fileName` | str | None | None |
| `$.dataTypes.app.files[*].globalName` | str | None | None |
| `$.dataTypes.app.files[*].count` | str | None | None |
| `$.dataTypes.birdwatchNote` | dict | None | None |
| `$.dataTypes.birdwatchNote.files` | list | None | None |
| `$.dataTypes.birdwatchNote.files[*]` | dict | None | None |
| `$.dataTypes.birdwatchNote.files[*].fileName` | str | None | None |
| `$.dataTypes.birdwatchNote.files[*].globalName` | str | None | None |
| `$.dataTypes.birdwatchNote.files[*].count` | str | None | None |
| `$.dataTypes.birdwatchNoteRating` | dict | None | None |
| `$.dataTypes.birdwatchNoteRating.files` | list | None | None |
| `$.dataTypes.birdwatchNoteRating.files[*]` | dict | None | None |
| `$.dataTypes.birdwatchNoteRating.files[*].fileName` | str | None | None |
| `$.dataTypes.birdwatchNoteRating.files[*].globalName` | str | None | None |
| `$.dataTypes.birdwatchNoteRating.files[*].count` | str | None | None |
| `$.dataTypes.block` | dict | None | None |
| `$.dataTypes.block.files` | list | None | None |
| `$.dataTypes.block.files[*]` | dict | None | None |
| `$.dataTypes.block.files[*].fileName` | str | None | None |
| `$.dataTypes.block.files[*].globalName` | str | None | None |
| `$.dataTypes.block.files[*].count` | str | None | None |
| `$.dataTypes.branchLinks` | dict | None | None |
| `$.dataTypes.branchLinks.files` | list | None | None |
| `$.dataTypes.branchLinks.files[*]` | dict | None | None |
| `$.dataTypes.branchLinks.files[*].fileName` | str | None | None |
| `$.dataTypes.branchLinks.files[*].globalName` | str | None | None |
| `$.dataTypes.branchLinks.files[*].count` | str | None | None |
| `$.dataTypes.communityTweet` | dict | None | None |
| `$.dataTypes.communityTweet.mediaDirectory` | str | None | None |
| `$.dataTypes.communityTweet.files` | list | None | None |
| `$.dataTypes.communityTweet.files[*]` | dict | None | None |
| `$.dataTypes.communityTweet.files[*].fileName` | str | None | None |
| `$.dataTypes.communityTweet.files[*].globalName` | str | None | None |
| `$.dataTypes.communityTweet.files[*].count` | str | None | None |
| `$.dataTypes.communityTweetMedia` | dict | None | None |
| `$.dataTypes.communityTweetMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.connectedApplication` | dict | None | None |
| `$.dataTypes.connectedApplication.files` | list | None | None |
| `$.dataTypes.connectedApplication.files[*]` | dict | None | None |
| `$.dataTypes.connectedApplication.files[*].fileName` | str | None | None |
| `$.dataTypes.connectedApplication.files[*].globalName` | str | None | None |
| `$.dataTypes.connectedApplication.files[*].count` | str | None | None |
| `$.dataTypes.contact` | dict | None | None |
| `$.dataTypes.contact.files` | list | None | None |
| `$.dataTypes.contact.files[*]` | dict | None | None |
| `$.dataTypes.contact.files[*].fileName` | str | None | None |
| `$.dataTypes.contact.files[*].globalName` | str | None | None |
| `$.dataTypes.contact.files[*].count` | str | None | None |
| `$.dataTypes.deviceToken` | dict | None | None |
| `$.dataTypes.deviceToken.files` | list | None | None |
| `$.dataTypes.deviceToken.files[*]` | dict | None | None |
| `$.dataTypes.deviceToken.files[*].fileName` | str | None | None |
| `$.dataTypes.deviceToken.files[*].globalName` | str | None | None |
| `$.dataTypes.deviceToken.files[*].count` | str | None | None |
| `$.dataTypes.directMessageGroupHeaders` | dict | None | None |
| `$.dataTypes.directMessageGroupHeaders.files` | list | None | None |
| `$.dataTypes.directMessageGroupHeaders.files[*]` | dict | None | None |
| `$.dataTypes.directMessageGroupHeaders.files[*].fileName` | str | None | None |
| `$.dataTypes.directMessageGroupHeaders.files[*].globalName` | str | None | None |
| `$.dataTypes.directMessageGroupHeaders.files[*].count` | str | None | None |
| `$.dataTypes.directMessageHeaders` | dict | None | None |
| `$.dataTypes.directMessageHeaders.files` | list | None | None |
| `$.dataTypes.directMessageHeaders.files[*]` | dict | None | None |
| `$.dataTypes.directMessageHeaders.files[*].fileName` | str | None | None |
| `$.dataTypes.directMessageHeaders.files[*].globalName` | str | None | None |
| `$.dataTypes.directMessageHeaders.files[*].count` | str | None | None |
| `$.dataTypes.directMessageMute` | dict | None | None |
| `$.dataTypes.directMessageMute.files` | list | None | None |
| `$.dataTypes.directMessageMute.files[*]` | dict | None | None |
| `$.dataTypes.directMessageMute.files[*].fileName` | str | None | None |
| `$.dataTypes.directMessageMute.files[*].globalName` | str | None | None |
| `$.dataTypes.directMessageMute.files[*].count` | str | None | None |
| `$.dataTypes.directMessages` | dict | None | None |
| `$.dataTypes.directMessages.mediaDirectory` | str | None | None |
| `$.dataTypes.directMessages.files` | list | None | None |
| `$.dataTypes.directMessages.files[*]` | dict | None | None |
| `$.dataTypes.directMessages.files[*].fileName` | str | None | None |
| `$.dataTypes.directMessages.files[*].globalName` | str | None | None |
| `$.dataTypes.directMessages.files[*].count` | str | None | None |
| `$.dataTypes.directMessagesGroup` | dict | None | None |
| `$.dataTypes.directMessagesGroup.mediaDirectory` | str | None | None |
| `$.dataTypes.directMessagesGroup.files` | list | None | None |
| `$.dataTypes.directMessagesGroup.files[*]` | dict | None | None |
| `$.dataTypes.directMessagesGroup.files[*].fileName` | str | None | None |
| `$.dataTypes.directMessagesGroup.files[*].globalName` | str | None | None |
| `$.dataTypes.directMessagesGroup.files[*].count` | str | None | None |
| `$.dataTypes.directMessagesGroupMedia` | dict | None | None |
| `$.dataTypes.directMessagesGroupMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.directMessagesMedia` | dict | None | None |
| `$.dataTypes.directMessagesMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.emailAddressChange` | dict | None | None |
| `$.dataTypes.emailAddressChange.files` | list | None | None |
| `$.dataTypes.emailAddressChange.files[*]` | dict | None | None |
| `$.dataTypes.emailAddressChange.files[*].fileName` | str | None | None |
| `$.dataTypes.emailAddressChange.files[*].globalName` | str | None | None |
| `$.dataTypes.emailAddressChange.files[*].count` | str | None | None |
| `$.dataTypes.follower` | dict | None | None |
| `$.dataTypes.follower.files` | list | None | None |
| `$.dataTypes.follower.files[*]` | dict | None | None |
| `$.dataTypes.follower.files[*].fileName` | str | None | None |
| `$.dataTypes.follower.files[*].globalName` | str | None | None |
| `$.dataTypes.follower.files[*].count` | str | None | None |
| `$.dataTypes.following` | dict | None | None |
| `$.dataTypes.following.files` | list | None | None |
| `$.dataTypes.following.files[*]` | dict | None | None |
| `$.dataTypes.following.files[*].fileName` | str | None | None |
| `$.dataTypes.following.files[*].globalName` | str | None | None |
| `$.dataTypes.following.files[*].count` | str | None | None |
| `$.dataTypes.ipAudit` | dict | None | None |
| `$.dataTypes.ipAudit.files` | list | None | None |
| `$.dataTypes.ipAudit.files[*]` | dict | None | None |
| `$.dataTypes.ipAudit.files[*].fileName` | str | None | None |
| `$.dataTypes.ipAudit.files[*].globalName` | str | None | None |
| `$.dataTypes.ipAudit.files[*].count` | str | None | None |
| `$.dataTypes.like` | dict | None | None |
| `$.dataTypes.like.files` | list | None | None |
| `$.dataTypes.like.files[*]` | dict | None | None |
| `$.dataTypes.like.files[*].fileName` | str | None | None |
| `$.dataTypes.like.files[*].globalName` | str | None | None |
| `$.dataTypes.like.files[*].count` | str | None | None |
| `$.dataTypes.listsCreated` | dict | None | None |
| `$.dataTypes.listsCreated.files` | list | None | None |
| `$.dataTypes.listsCreated.files[*]` | dict | None | None |
| `$.dataTypes.listsCreated.files[*].fileName` | str | None | None |
| `$.dataTypes.listsCreated.files[*].globalName` | str | None | None |
| `$.dataTypes.listsCreated.files[*].count` | str | None | None |
| `$.dataTypes.listsMember` | dict | None | None |
| `$.dataTypes.listsMember.files` | list | None | None |
| `$.dataTypes.listsMember.files[*]` | dict | None | None |
| `$.dataTypes.listsMember.files[*].fileName` | str | None | None |
| `$.dataTypes.listsMember.files[*].globalName` | str | None | None |
| `$.dataTypes.listsMember.files[*].count` | str | None | None |
| `$.dataTypes.listsSubscribed` | dict | None | None |
| `$.dataTypes.listsSubscribed.files` | list | None | None |
| `$.dataTypes.listsSubscribed.files[*]` | dict | None | None |
| `$.dataTypes.listsSubscribed.files[*].fileName` | str | None | None |
| `$.dataTypes.listsSubscribed.files[*].globalName` | str | None | None |
| `$.dataTypes.listsSubscribed.files[*].count` | str | None | None |
| `$.dataTypes.moment` | dict | None | None |
| `$.dataTypes.moment.mediaDirectory` | str | None | None |
| `$.dataTypes.moment.files` | list | None | None |
| `$.dataTypes.moment.files[*]` | dict | None | None |
| `$.dataTypes.moment.files[*].fileName` | str | None | None |
| `$.dataTypes.moment.files[*].globalName` | str | None | None |
| `$.dataTypes.moment.files[*].count` | str | None | None |
| `$.dataTypes.momentsMedia` | dict | None | None |
| `$.dataTypes.momentsMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.momentsTweetsMedia` | dict | None | None |
| `$.dataTypes.momentsTweetsMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.mute` | dict | None | None |
| `$.dataTypes.mute.files` | list | None | None |
| `$.dataTypes.mute.files[*]` | dict | None | None |
| `$.dataTypes.mute.files[*].fileName` | str | None | None |
| `$.dataTypes.mute.files[*].globalName` | str | None | None |
| `$.dataTypes.mute.files[*].count` | str | None | None |
| `$.dataTypes.niDevices` | dict | None | None |
| `$.dataTypes.niDevices.files` | list | None | None |
| `$.dataTypes.niDevices.files[*]` | dict | None | None |
| `$.dataTypes.niDevices.files[*].fileName` | str | None | None |
| `$.dataTypes.niDevices.files[*].globalName` | str | None | None |
| `$.dataTypes.niDevices.files[*].count` | str | None | None |
| `$.dataTypes.periscopeAccountInformation` | dict | None | None |
| `$.dataTypes.periscopeAccountInformation.files` | list | None | None |
| `$.dataTypes.periscopeAccountInformation.files[*]` | dict | None | None |
| `$.dataTypes.periscopeAccountInformation.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeAccountInformation.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeAccountInformation.files[*].count` | str | None | None |
| `$.dataTypes.periscopeBanInformation` | dict | None | None |
| `$.dataTypes.periscopeBanInformation.files` | list | None | None |
| `$.dataTypes.periscopeBanInformation.files[*]` | dict | None | None |
| `$.dataTypes.periscopeBanInformation.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeBanInformation.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeBanInformation.files[*].count` | str | None | None |
| `$.dataTypes.periscopeBroadcastMetadata` | dict | None | None |
| `$.dataTypes.periscopeBroadcastMetadata.files` | list | None | None |
| `$.dataTypes.periscopeBroadcastMetadata.files[*]` | dict | None | None |
| `$.dataTypes.periscopeBroadcastMetadata.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeBroadcastMetadata.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeBroadcastMetadata.files[*].count` | str | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser` | dict | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser.files` | list | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser.files[*]` | dict | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeCommentsMadeByUser.files[*].count` | str | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts` | dict | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts.files` | list | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts.files[*]` | dict | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeExpiredBroadcasts.files[*].count` | str | None | None |
| `$.dataTypes.periscopeFollowers` | dict | None | None |
| `$.dataTypes.periscopeFollowers.files` | list | None | None |
| `$.dataTypes.periscopeFollowers.files[*]` | dict | None | None |
| `$.dataTypes.periscopeFollowers.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeFollowers.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeFollowers.files[*].count` | str | None | None |
| `$.dataTypes.periscopeProfileDescription` | dict | None | None |
| `$.dataTypes.periscopeProfileDescription.files` | list | None | None |
| `$.dataTypes.periscopeProfileDescription.files[*]` | dict | None | None |
| `$.dataTypes.periscopeProfileDescription.files[*].fileName` | str | None | None |
| `$.dataTypes.periscopeProfileDescription.files[*].globalName` | str | None | None |
| `$.dataTypes.periscopeProfileDescription.files[*].count` | str | None | None |
| `$.dataTypes.personalization` | dict | None | None |
| `$.dataTypes.personalization.files` | list | None | None |
| `$.dataTypes.personalization.files[*]` | dict | None | None |
| `$.dataTypes.personalization.files[*].fileName` | str | None | None |
| `$.dataTypes.personalization.files[*].globalName` | str | None | None |
| `$.dataTypes.personalization.files[*].count` | str | None | None |
| `$.dataTypes.phoneNumber` | dict | None | None |
| `$.dataTypes.phoneNumber.files` | list | None | None |
| `$.dataTypes.phoneNumber.files[*]` | dict | None | None |
| `$.dataTypes.phoneNumber.files[*].fileName` | str | None | None |
| `$.dataTypes.phoneNumber.files[*].globalName` | str | None | None |
| `$.dataTypes.phoneNumber.files[*].count` | str | None | None |
| `$.dataTypes.professionalData` | dict | None | None |
| `$.dataTypes.professionalData.files` | list | None | None |
| `$.dataTypes.professionalData.files[*]` | dict | None | None |
| `$.dataTypes.professionalData.files[*].fileName` | str | None | None |
| `$.dataTypes.professionalData.files[*].globalName` | str | None | None |
| `$.dataTypes.professionalData.files[*].count` | str | None | None |
| `$.dataTypes.profile` | dict | None | None |
| `$.dataTypes.profile.mediaDirectory` | str | None | None |
| `$.dataTypes.profile.files` | list | None | None |
| `$.dataTypes.profile.files[*]` | dict | None | None |
| `$.dataTypes.profile.files[*].fileName` | str | None | None |
| `$.dataTypes.profile.files[*].globalName` | str | None | None |
| `$.dataTypes.profile.files[*].count` | str | None | None |
| `$.dataTypes.profileMedia` | dict | None | None |
| `$.dataTypes.profileMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.protectedHistory` | dict | None | None |
| `$.dataTypes.protectedHistory.files` | list | None | None |
| `$.dataTypes.protectedHistory.files[*]` | dict | None | None |
| `$.dataTypes.protectedHistory.files[*].fileName` | str | None | None |
| `$.dataTypes.protectedHistory.files[*].globalName` | str | None | None |
| `$.dataTypes.protectedHistory.files[*].count` | str | None | None |
| `$.dataTypes.replyPrompt` | dict | None | None |
| `$.dataTypes.replyPrompt.files` | list | None | None |
| `$.dataTypes.replyPrompt.files[*]` | dict | None | None |
| `$.dataTypes.replyPrompt.files[*].fileName` | str | None | None |
| `$.dataTypes.replyPrompt.files[*].globalName` | str | None | None |
| `$.dataTypes.replyPrompt.files[*].count` | str | None | None |
| `$.dataTypes.savedSearch` | dict | None | None |
| `$.dataTypes.savedSearch.files` | list | None | None |
| `$.dataTypes.savedSearch.files[*]` | dict | None | None |
| `$.dataTypes.savedSearch.files[*].fileName` | str | None | None |
| `$.dataTypes.savedSearch.files[*].globalName` | str | None | None |
| `$.dataTypes.savedSearch.files[*].count` | str | None | None |
| `$.dataTypes.screenNameChange` | dict | None | None |
| `$.dataTypes.screenNameChange.files` | list | None | None |
| `$.dataTypes.screenNameChange.files[*]` | dict | None | None |
| `$.dataTypes.screenNameChange.files[*].fileName` | str | None | None |
| `$.dataTypes.screenNameChange.files[*].globalName` | str | None | None |
| `$.dataTypes.screenNameChange.files[*].count` | str | None | None |
| `$.dataTypes.smartblock` | dict | None | None |
| `$.dataTypes.smartblock.files` | list | None | None |
| `$.dataTypes.smartblock.files[*]` | dict | None | None |
| `$.dataTypes.smartblock.files[*].fileName` | str | None | None |
| `$.dataTypes.smartblock.files[*].globalName` | str | None | None |
| `$.dataTypes.smartblock.files[*].count` | str | None | None |
| `$.dataTypes.spacesMetadata` | dict | None | None |
| `$.dataTypes.spacesMetadata.files` | list | None | None |
| `$.dataTypes.spacesMetadata.files[*]` | dict | None | None |
| `$.dataTypes.spacesMetadata.files[*].fileName` | str | None | None |
| `$.dataTypes.spacesMetadata.files[*].globalName` | str | None | None |
| `$.dataTypes.spacesMetadata.files[*].count` | str | None | None |
| `$.dataTypes.sso` | dict | None | None |
| `$.dataTypes.sso.files` | list | None | None |
| `$.dataTypes.sso.files[*]` | dict | None | None |
| `$.dataTypes.sso.files[*].fileName` | str | None | None |
| `$.dataTypes.sso.files[*].globalName` | str | None | None |
| `$.dataTypes.sso.files[*].count` | str | None | None |
| `$.dataTypes.tweet` | dict | None | None |
| `$.dataTypes.tweet.mediaDirectory` | str | None | None |
| `$.dataTypes.tweet.files` | list | None | None |
| `$.dataTypes.tweet.files[*]` | dict | None | None |
| `$.dataTypes.tweet.files[*].fileName` | str | None | None |
| `$.dataTypes.tweet.files[*].globalName` | str | None | None |
| `$.dataTypes.tweet.files[*].count` | str | None | None |
| `$.dataTypes.tweetMedia` | dict | None | None |
| `$.dataTypes.tweetMedia.mediaDirectory` | str | None | None |
| `$.dataTypes.tweetdeck` | dict | None | None |
| `$.dataTypes.tweetdeck.files` | list | None | None |
| `$.dataTypes.tweetdeck.files[*]` | dict | None | None |
| `$.dataTypes.tweetdeck.files[*].fileName` | str | None | None |
| `$.dataTypes.tweetdeck.files[*].globalName` | str | None | None |
| `$.dataTypes.tweetdeck.files[*].count` | str | None | None |
| `$.dataTypes.userLinkClicks` | dict | None | None |
| `$.dataTypes.userLinkClicks.files` | list | None | None |
| `$.dataTypes.userLinkClicks.files[*]` | dict | None | None |
| `$.dataTypes.userLinkClicks.files[*].fileName` | str | None | None |
| `$.dataTypes.userLinkClicks.files[*].globalName` | str | None | None |
| `$.dataTypes.userLinkClicks.files[*].count` | str | None | None |
| `$.dataTypes.verified` | dict | None | None |
| `$.dataTypes.verified.files` | list | None | None |
| `$.dataTypes.verified.files[*]` | dict | None | None |
| `$.dataTypes.verified.files[*].fileName` | str | None | None |
| `$.dataTypes.verified.files[*].globalName` | str | None | None |
| `$.dataTypes.verified.files[*].count` | str | None | None |

### `data/moment.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/mute.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].muting` | dict | None | None |
| `$[*].muting.accountId` | str | None | None |
| `$[*].muting.userLink` | str | None | None |

### `data/ni-devices.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].niDeviceResponse` | dict | None | None |
| `$[*].niDeviceResponse.pushDevice` | dict | None | None |
| `$[*].niDeviceResponse.pushDevice.deviceVersion` | str | None | None |
| `$[*].niDeviceResponse.pushDevice.udid` | str | None | None |
| `$[*].niDeviceResponse.pushDevice.deviceType` | str | None | None |
| `$[*].niDeviceResponse.pushDevice.token` | str | None | None |
| `$[*].niDeviceResponse.pushDevice.updatedDate` | str | None | None |
| `$[*].niDeviceResponse.pushDevice.createdDate` | str | None | None |
| `$[*].niDeviceResponse.messagingDevice` | dict | None | None |
| `$[*].niDeviceResponse.messagingDevice.phoneNumber` | str | None | None |
| `$[*].niDeviceResponse.messagingDevice.carrier` | str | None | None |
| `$[*].niDeviceResponse.messagingDevice.deviceType` | str | None | None |
| `$[*].niDeviceResponse.messagingDevice.updatedDate` | str | None | None |
| `$[*].niDeviceResponse.messagingDevice.createdDate` | str | None | None |

### `data/periscope-account-information.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].periscopeAccountInformation` | dict | None | None |
| `$[*].periscopeAccountInformation.displayName` | str | None | None |
| `$[*].periscopeAccountInformation.digitsId` | str | None | None |
| `$[*].periscopeAccountInformation.username` | str | None | None |
| `$[*].periscopeAccountInformation.twitterId` | str | None | None |
| `$[*].periscopeAccountInformation.id` | str | None | None |
| `$[*].periscopeAccountInformation.twitterScreenName` | str | None | None |
| `$[*].periscopeAccountInformation.isTwitterUser` | bool | None | None |
| `$[*].periscopeAccountInformation.createdAt` | str | None | None |

### `data/periscope-ban-information.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].periscopeBanInformation` | dict | None | None |

### `data/periscope-broadcast-metadata.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/periscope-comments-made-by-user.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/periscope-expired-broadcasts.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/periscope-followers.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/periscope-profile-description.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].periscopeProfileDescription` | dict | None | None |
| `$[*].periscopeProfileDescription.bio` | str | None | None |

### `data/personalization.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].p13nData` | dict | None | None |
| `$[*].p13nData.demographics` | dict | None | None |
| `$[*].p13nData.demographics.languages` | list | None | None |
| `$[*].p13nData.demographics.languages[*]` | dict | None | None |
| `$[*].p13nData.demographics.languages[*].language` | str | None | None |
| `$[*].p13nData.demographics.languages[*].isDisabled` | bool | None | None |
| `$[*].p13nData.demographics.genderInfo` | dict | None | None |
| `$[*].p13nData.demographics.genderInfo.gender` | str | None | None |
| `$[*].p13nData.interests` | dict | None | None |
| `$[*].p13nData.interests.interests` | list | None | None |
| `$[*].p13nData.interests.interests[*]` | dict | None | None |
| `$[*].p13nData.interests.interests[*].name` | str | None | None |
| `$[*].p13nData.interests.interests[*].isDisabled` | bool | None | None |
| `$[*].p13nData.interests.partnerInterests` | list | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers` | dict | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers.numAudiences` | str | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers.advertisers` | list | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers.lookalikeAdvertisers` | list | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers.lookalikeAdvertisers[*]` | str | None | None |
| `$[*].p13nData.interests.audienceAndAdvertisers.doNotReachAdvertisers` | list | None | None |
| `$[*].p13nData.interests.shows` | list | None | None |
| `$[*].p13nData.interests.shows[*]` | str | None | None |
| `$[*].p13nData.locationHistory` | list | None | None |
| `$[*].p13nData.inferredAgeInfo` | dict | None | None |
| `$[*].p13nData.inferredAgeInfo.age` | list | None | None |
| `$[*].p13nData.inferredAgeInfo.age[*]` | str | None | None |
| `$[*].p13nData.inferredAgeInfo.birthDate` | str | None | None |

### `data/phone-number.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].device` | dict | None | None |
| `$[*].device.phoneNumber` | str | None | None |

### `data/professional-data.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/profile.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].profile` | dict | None | None |
| `$[*].profile.description` | dict | None | None |
| `$[*].profile.description.bio` | str | None | None |
| `$[*].profile.description.website` | str | None | None |
| `$[*].profile.description.location` | str | None | None |
| `$[*].profile.avatarMediaUrl` | str | None | None |
| `$[*].profile.headerMediaUrl` | str | None | None |

### `data/protected-history.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/reply-prompt.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/saved-search.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/screen-name-change.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].screenNameChange` | dict | None | None |
| `$[*].screenNameChange.accountId` | str | None | None |
| `$[*].screenNameChange.screenNameChange` | dict | None | None |
| `$[*].screenNameChange.screenNameChange.changedAt` | str | None | None |
| `$[*].screenNameChange.screenNameChange.changedFrom` | str | None | None |
| `$[*].screenNameChange.screenNameChange.changedTo` | str | None | None |

### `data/smartblock.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/spaces-metadata.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/sso.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/tweet.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].tweet` | dict | None | None |
| `$[*].tweet.retweeted` | bool | None | None |
| `$[*].tweet.source` | str | None | None |
| `$[*].tweet.entities` | dict | None | None |
| `$[*].tweet.entities.hashtags` | list | None | None |
| `$[*].tweet.entities.hashtags[*]` | dict | None | None |
| `$[*].tweet.entities.hashtags[*].text` | str | None | None |
| `$[*].tweet.entities.hashtags[*].indices` | list | None | None |
| `$[*].tweet.entities.hashtags[*].indices[*]` | str | None | None |
| `$[*].tweet.entities.symbols` | list | None | None |
| `$[*].tweet.entities.user_mentions` | list | None | None |
| `$[*].tweet.entities.user_mentions[*]` | dict | None | None |
| `$[*].tweet.entities.user_mentions[*].name` | str | None | None |
| `$[*].tweet.entities.user_mentions[*].screen_name` | str | None | None |
| `$[*].tweet.entities.user_mentions[*].indices` | list | None | None |
| `$[*].tweet.entities.user_mentions[*].indices[*]` | str | None | None |
| `$[*].tweet.entities.user_mentions[*].id_str` | str | None | None |
| `$[*].tweet.entities.user_mentions[*].id` | str | None | None |
| `$[*].tweet.entities.urls` | list | None | None |
| `$[*].tweet.entities.urls[*]` | dict | None | None |
| `$[*].tweet.entities.urls[*].url` | str | None | None |
| `$[*].tweet.entities.urls[*].expanded_url` | str | None | None |
| `$[*].tweet.entities.urls[*].display_url` | str | None | None |
| `$[*].tweet.entities.urls[*].indices` | list | None | None |
| `$[*].tweet.entities.urls[*].indices[*]` | str | None | None |
| `$[*].tweet.entities.media` | list | None | None |
| `$[*].tweet.entities.media[*]` | dict | None | None |
| `$[*].tweet.entities.media[*].expanded_url` | str | None | None |
| `$[*].tweet.entities.media[*].source_status_id` | str | None | None |
| `$[*].tweet.entities.media[*].indices` | list | None | None |
| `$[*].tweet.entities.media[*].indices[*]` | str | None | None |
| `$[*].tweet.entities.media[*].url` | str | None | None |
| `$[*].tweet.entities.media[*].media_url` | str | None | None |
| `$[*].tweet.entities.media[*].id_str` | str | None | None |
| `$[*].tweet.entities.media[*].source_user_id` | str | None | None |
| `$[*].tweet.entities.media[*].id` | str | None | None |
| `$[*].tweet.entities.media[*].media_url_https` | str | None | None |
| `$[*].tweet.entities.media[*].source_user_id_str` | str | None | None |
| `$[*].tweet.entities.media[*].sizes` | dict | None | None |
| `$[*].tweet.entities.media[*].sizes.thumb` | dict | None | None |
| `$[*].tweet.entities.media[*].sizes.thumb.w` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.thumb.h` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.thumb.resize` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.medium` | dict | None | None |
| `$[*].tweet.entities.media[*].sizes.medium.w` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.medium.h` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.medium.resize` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.small` | dict | None | None |
| `$[*].tweet.entities.media[*].sizes.small.w` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.small.h` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.small.resize` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.large` | dict | None | None |
| `$[*].tweet.entities.media[*].sizes.large.w` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.large.h` | str | None | None |
| `$[*].tweet.entities.media[*].sizes.large.resize` | str | None | None |
| `$[*].tweet.entities.media[*].type` | str | None | None |
| `$[*].tweet.entities.media[*].source_status_id_str` | str | None | None |
| `$[*].tweet.entities.media[*].display_url` | str | None | None |
| `$[*].tweet.display_text_range` | list | None | None |
| `$[*].tweet.display_text_range[*]` | str | None | None |
| `$[*].tweet.favorite_count` | str | None | None |
| `$[*].tweet.in_reply_to_status_id_str` | str | None | None |
| `$[*].tweet.id_str` | str | None | None |
| `$[*].tweet.in_reply_to_user_id` | str | None | None |
| `$[*].tweet.truncated` | bool | None | None |
| `$[*].tweet.retweet_count` | str | None | None |
| `$[*].tweet.id` | str | None | None |
| `$[*].tweet.in_reply_to_status_id` | str | None | None |
| `$[*].tweet.created_at` | str | None | None |
| `$[*].tweet.favorited` | bool | None | None |
| `$[*].tweet.full_text` | str | None | None |
| `$[*].tweet.lang` | str | None | None |
| `$[*].tweet.in_reply_to_screen_name` | str | None | None |
| `$[*].tweet.in_reply_to_user_id_str` | str | None | None |
| `$[*].tweet.possibly_sensitive` | bool | None | None |
| `$[*].tweet.extended_entities` | dict | None | None |
| `$[*].tweet.extended_entities.media` | list | None | None |
| `$[*].tweet.extended_entities.media[*]` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].expanded_url` | str | None | None |
| `$[*].tweet.extended_entities.media[*].source_status_id` | str | None | None |
| `$[*].tweet.extended_entities.media[*].indices` | list | None | None |
| `$[*].tweet.extended_entities.media[*].indices[*]` | str | None | None |
| `$[*].tweet.extended_entities.media[*].url` | str | None | None |
| `$[*].tweet.extended_entities.media[*].media_url` | str | None | None |
| `$[*].tweet.extended_entities.media[*].id_str` | str | None | None |
| `$[*].tweet.extended_entities.media[*].video_info` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.aspect_ratio` | list | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.aspect_ratio[*]` | str | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.duration_millis` | str | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.variants` | list | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.variants[*]` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.variants[*].bitrate` | str | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.variants[*].content_type` | str | None | None |
| `$[*].tweet.extended_entities.media[*].video_info.variants[*].url` | str | None | None |
| `$[*].tweet.extended_entities.media[*].source_user_id` | str | None | None |
| `$[*].tweet.extended_entities.media[*].additional_media_info` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].additional_media_info.monetizable` | bool | None | None |
| `$[*].tweet.extended_entities.media[*].additional_media_info.title` | str | None | None |
| `$[*].tweet.extended_entities.media[*].additional_media_info.description` | str | None | None |
| `$[*].tweet.extended_entities.media[*].additional_media_info.embeddable` | bool | None | None |
| `$[*].tweet.extended_entities.media[*].id` | str | None | None |
| `$[*].tweet.extended_entities.media[*].media_url_https` | str | None | None |
| `$[*].tweet.extended_entities.media[*].source_user_id_str` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.thumb` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.thumb.w` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.thumb.h` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.thumb.resize` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.medium` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.medium.w` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.medium.h` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.medium.resize` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.small` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.small.w` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.small.h` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.small.resize` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.large` | dict | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.large.w` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.large.h` | str | None | None |
| `$[*].tweet.extended_entities.media[*].sizes.large.resize` | str | None | None |
| `$[*].tweet.extended_entities.media[*].type` | str | None | None |
| `$[*].tweet.extended_entities.media[*].source_status_id_str` | str | None | None |
| `$[*].tweet.extended_entities.media[*].display_url` | str | None | None |

### `data/tweetdeck.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |

### `data/user-link-clicks.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].userInteractionsData` | dict | None | None |
| `$[*].userInteractionsData.linkClick` | dict | None | None |
| `$[*].userInteractionsData.linkClick.tweetId` | str | None | None |
| `$[*].userInteractionsData.linkClick.finalUrl` | str | None | None |
| `$[*].userInteractionsData.linkClick.timeStampOfInteraction` | str | None | None |

### `data/verified.js`

| path | foundType | descriptiveType | description |
|---|---|---|---|
| `$` | RootNode | None | None |
| `$[*]` | dict | None | None |
| `$[*].verified` | dict | None | None |
| `$[*].verified.accountId` | str | None | None |
| `$[*].verified.verified` | bool | None | None |

