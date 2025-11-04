---
blurb: Set mutable properties for an MPT.
labels:
 - Multi-purpose Tokens, MPTs
---
# MPTokenIssuanceSet
[[Source]](https://github.com/XRPLF/rippled/blob/master/src/xrpld/app/tx/detail/MPTokenIssuanceSet.cpp "Source")

Use this transaction to update a mutable property for a Multi-purpose Token. The transaction flags determine which change(s) to apply.

{% amendment-disclaimer name="MPTokensV1" /%}

## Example

```json 
{
      "TransactionType": "MPTokenIssuanceSet",
      "Fee": "10",
      "MPTokenIssuanceID": "00070C4495F14B0E44F78A264E41713C64B5F89242540EE255534400000000000000",
      "Flags": 1
}
```

<!-- ## MPTokenIssuanceSet Fields -->

{% raw-partial file="/docs/_snippets/tx-fields-intro.md" /%}

| Field               | JSON Type            | [Internal Type][] | Required? | Description |
|:--------------------|:---------------------|:------------------|:----------|-------------|
| `DomainID`          | String - [Hash][]    | UInt256           | No        | The ledger entry ID of a permissioned domain that will manage access to the MPT. An empy value or `0` will remove permissioned domain access management. Any accounts that lose access to the MPT because of `DomainID` updates--unless explicitly authorized by the MPT issuer--lose the ability to send or receive MPTs they already hold. The `tfMPTRequireAuth` flag must have been set in the `MPTokenIssuanceCreate` transaction to use permissioned domains.<br>{% amendment-disclaimer name="PermissionedDomains" /%}<br>{% amendment-disclaimer name="SingleAssetVault" /%} |
| `MPTokenIssuanceID` | String - Hexadecimal | UInt192           | Yes       | The identifier of the `MPTokenIssuance` to update. |
| `Holder`            | String - [Address][] | AccountID         | No        | An individual token holder. If provided, apply changes to the given holder's balance of the given MPT issuance. If omitted, apply to all accounts holding the given MPT issuance. |

### MPTokenIssuanceSet Flags

Transactions of the `MPTokenIssuanceSet` type support additional values in the `Flags` field, as follows:

| Flag Name          | Hex Value    | Decimal Value | Description                   |
|:-------------------|:-------------|:--------------|:------------------------------|
| `tfMPTLock`        | `0x00000001` | 1             | Enable to lock balances of this MPT issuance. |
| `tfMPTUnlock`      | `0x00000002` | 2             | Enable to unlock balances of this MPT issuance. |

## Error Cases

Besides errors that can occur for all transactions, {% $frontmatter.seo.title %} transactions can result in the following [transaction result codes](../transaction-results/index.md):

| Error Code                | Description |
|:--------------------------|:------------|
| `temDISABLED`             | The `MPTokensV1` amendment is disabled. You will also receive this error if you include a `DomainID` field in the transaction, but the `PermissionedDomains` and `SingleAssetVault` amendments are both disabled. |
| `tecNO_DELEGATE_PERMISSION` | You are attempting to use a delegate account with insufficient permissions to submit this transaction. |
| `tecNO_DST`               | The account specified in the `Holder` field doesn't exist. |
| `tecNO_PERMISSION`        | - The `lsfMPTCanLock` flag isn't enabled, but you are attempting to lock or unlock an MPT.<br>- The `SingleAssetVault` amendment is disabled and you're trying to modify a `DomainID` field. | 
| `temMALFORMED`            | - You specified a `DomainID` and `Holder` value--only one can be set in a single transaction.<br>- You specified the same account for both `Acount` and `Holder`.<br>- The transaction isn't changing anything; it must either update a flag or modify the `DomainID`. |
| `tecOBJECT_NOT_FOUND`    | The specified `MPToken`, `MPTokenIssuance`, or `PermissionedDomain` ledger entry doesn't exist. |

{% raw-partial file="/docs/_snippets/common-links.md" /%}
