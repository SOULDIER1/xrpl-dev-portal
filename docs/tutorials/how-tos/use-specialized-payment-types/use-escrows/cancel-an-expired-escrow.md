---
seo:
    description: Cancel an expired escrow.
labels:
  - Escrow
---
# Cancel an Expired Escrow

This tutorial demonstrates how to cancel an [escrow](../../../../concepts/payment-types/escrow.md) that has passed its expiration time. You can use this to reclaim funds that you escrowed but were never claimed by the recipient.

## Goals

By following this tutorial, you should learn how to:

- Compare a timestamp from the ledger to the current time.
- Cancel an expired escrow.

## Prerequisites

To complete this tutorial, you should:

- Have a basic understanding of the XRP Ledger.
- Have an XRP Ledger client library, such as **xrpl.js**, installed.
- Already know how to send a [timed](./send-a-timed-escrow.md) or [conditional](./send-a-conditional-escrow.md) escrow.

## Source Code

You can find the complete source code for this tutorial's examples in the {% repo-link path="_code-samples/escrow/" %}code samples section of this website's repository{% /repo-link %}.

##  Steps

### 1. Install dependencies

{% tabs %}
{% tab label="JavaScript" %}
From the code sample folder, use `npm` to install dependencies:

```sh
npm i
```
{% /tab %}

{% tab label="Python" %}
From the code sample folder, set up a virtual environment and use `pip` to install dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
{% /tab %}
{% /tabs %}

***TODO: finish refactoring***










An escrow in the XRP Ledger is expired when its `CancelAfter` time is lower than the `close_time` of the latest validated ledger. Escrows without a `CancelAfter` time never expire.

## 1. Get the latest validated ledger

Use the [ledger method][] to look up the latest validated ledger and get the `close_time` value.

Request:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/ledger-request-expiration.json" language="json" /%}
{% /tab %}

{% /tabs %}

Response:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/ledger-response-expiration.json" language="json" /%}
{% /tab %}

{% /tabs %}

## 2. Look up the escrow

Use the [account_objects method][] and compare `CancelAfter` to `close_time`:

Request:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/account_objects-request-expiration.json" language="json" /%}
{% /tab %}

{% /tabs %}

Response:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/account_objects-response-expiration.json" language="json" /%}
{% /tab %}

{% /tabs %}

## 3. Submit EscrowCancel transaction

***Anyone*** can cancel an expired escrow in the XRP Ledger by sending an [EscrowCancel transaction][]. Set the `Owner` field of the transaction to the `Account` of the `EscrowCreate` transaction that created this escrow. Set the `OfferSequence` field to the `Sequence` of the `EscrowCreate` transaction.

{% admonition type="success" name="Tip" %}If you don't know what `OfferSequence` to use, you can look up the transaction that created the Escrow: call the [tx method][] with the value of the Escrow's `PreviousTxnID` field. In `tx` response, use the `Sequence` value of that transaction as the `OfferSequence` value of the EscrowCancel transaction.{% /admonition %}

{% partial file="/docs/_snippets/secret-key-warning.md" /%} 

{% tabs %}

{% tab label="Websocket" %}
Request:
{% code-snippet file="/_api-examples/escrow/websocket/submit-request-escrowcancel.json" language="json" /%}

Response:
{% code-snippet file="/_api-examples/escrow/websocket/submit-response-escrowcancel.json" language="json" /%}
{% /tab %}

{% tab label="Javascript" %}
{% code-snippet file="/_code-samples/escrow/js/cancel-escrow.js" language="js" from="const escrowCancelTransaction" before="await client.disconnect" /%}
{% /tab %}

{% tab label="Python" %}
{% code-snippet file="/_code-samples/escrow/py/cancel_escrow.py" language="py"  from="# Build escrow cancel" /%}
{% /tab %}

{% /tabs %}

Take note of the transaction's identifying `hash` value so you can check its final status when it is included in a validated ledger version.

## 4. Wait for validation

{% raw-partial file="/docs/_snippets/wait-for-validation.md" /%}

## 5. Confirm final result

Use the [tx method][] with the `EscrowCancel` transaction's identifying hash to check its final status. Look in the transaction metadata for a `DeletedNode` with `LedgerEntryType` of `Escrow`. Also look for a `ModifiedNode` of type `AccountRoot` for the sender of the escrowed payment. The `FinalFields` of the object should show the increase in XRP in the `Balance` field for the returned XRP.

Request:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/tx-request-escrowcancel.json" language="json" /%}
{% /tab %}

{% /tabs %}

Response:

{% tabs %}

{% tab label="Websocket" %}
{% code-snippet file="/_api-examples/escrow/websocket/tx-response-escrowcancel.json" language="json" /%}
{% /tab %}

{% /tabs %}

In the above example, `r3wN3v2vTUkr5qd6daqDc2xE4LSysdVjkT` is the sender of the escrow, and the increase in `Balance` from 99999**8**9990 drops to 99999**9**9990 drops represents the return of the escrowed 10,000 drops of XRP (0.01 XRP).


## See Also

- **Concepts:**
    - [What is XRP?](../../../../introduction/what-is-xrp.md)
    - [Payment Types](../../../../concepts/payment-types/index.md)
        - [Escrow](../../../../concepts/payment-types/escrow.md)
- **Tutorials:**
    - [Send XRP](../../send-xrp.md)
    - [Look Up Transaction Results](../../../../concepts/transactions/finality-of-results/look-up-transaction-results.md)
    - [Reliable Transaction Submission](../../../../concepts/transactions/reliable-transaction-submission.md)
- **References:**
    - [EscrowCancel transaction][]
    - [EscrowCreate transaction][]
    - [EscrowFinish transaction][]
    - [account_objects method][]
    - [tx method][]
    - [Escrow ledger object](../../../../references/protocol/ledger-data/ledger-entry-types/escrow.md)

{% raw-partial file="/docs/_snippets/common-links.md" /%}
