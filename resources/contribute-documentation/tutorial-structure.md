---
seo:
    description: A summary of the parts of a standard tutorial.
---
# Tutorial Template

This tutorial demonstrates the structure of a **[tutorial](./tutorial-guidelines.md)** in the XRPL.org standard style, including:

- Typical headings for a tutorial page
- Recommendations for code samples and usage
- Options and variations

You may also want to add a small amount of additional context of _why_ or _when_ you would want to do these things. Don't go overboard—leave the details for concept or use case articles.

The template should begin with an intro that states what the tutorial is about and has a "backlink" to the conceptual documentation for the core concepts/features that the tutorial demonstrates.

## Goals

By following this template, you should be able to:

- Create tutorials in a style that's consistent with the rest of the site.
- Remember to include all the important parts of a tutorial, and minimize digressions.
- Provide sample code that both humans and machines can copy and adapt for their purposes, with enough context to help them do so.

If the tutorial includes a graphical interface, include a screenshot of the final product here.

## Prerequisites

To complete this tutorial, you should meet the following guidelines:

- You have a local clone of the [xrpl-dev-portal](https://github.com/XRPLF/xrpl-dev-portal/) git repository.
- You have an appropiate text/code editor installed, such as [Visual Studio Code](https://code.visualstudio.com/).
- You are familiar with the [Contribution and Style Guidelines](./index.md) for XRPL Documentation.

{% admonition type="info" name="About prerequisites" %}
Prerequisites can take several forms: 

- Knowledge and learning background, especially tutorials that this one builds on top of.
- Dev environment setup, especially basic depedencies such as your xrpl client library.
    - Do not include dependencies that are specific to this tutorial here, because people tend to skim/gloss over this section. For dependencies specific to this tutorial, include them in the steps later.
- Specific on-chain structures that need to be in place in advance. For example, to trade against an AMM, the AMM must exist in the ledger.
- Amendments that need to be enabled for this tutorial. Use an amendment disclaimer component to show the Mainnet status of the amendment.
{% /admonition %}

## Source Code

You can find the complete source code for this tutorial's examples in the {% repo-link path="resources/contribute-documentation/tutorial-structure.md" %}resources section of this website's repository{% /repo-link %}.

{% admonition type="success" name="Tip" %}
Use the `{% repo-link ... %}` component to link to the source files; this component is designed to adjust based on the environment, so for example previews link to the code on the preview branch... although it doesn't fully work as of this writing (2025-08-11).
{% /admonition %}

## Usage

To test that the code runs properly, you can navigate to the repository top and start the local Redocly server as follows:

```sh
npm run start
```

Then, navigate to <http://localhost:4000/resources/contribute-documentation/tutorial-structure> to view the parsed version of this page.

{% admonition type="info" name="Usage is optional" %}
You should include a Usage section in **sample app tutorials**, including commandline utilities that have multiple options, or multiple scripts that need to be run in a specific order. If there's a user interface, you can also embed a video demonstrating usage of the sample app.

For single-file code samples that perform a linear set of steps, you can omit the Usage section.
{% /admonition %}

## Steps

Follow these steps to build a tutorial.

### Install Dependencies

Unlike the ones in Prerequisites, this step is for dependencies that are specific to this tutorial. They're here because people tend to gloss over the preamble parts and skip straight to the "meat" of the tutorial.

{% tabs %}
{% tab label="JavaScript" %}
From the code sample folder, use npm to install dependencies:

```sh
npm i
```
{% /tab %}
{% tab label="Python" %}
From the code sample folder, use pip to install dependencies:

```sh
pip install -r requirements.txt
```
{% /tab %}
{% /tabs %}

{% admonition type="warning" name="Dependencies and maintenance burden" %}
Dependencies can be a source of maintenance burden, as you need to keep updating them to stay up-to-date with security fixes and breaking changes to the dependencies. On the other hand, reimplementing common utilities in every code sample is its own maintenance burden, and it's even worse to "roll your own" security-sensitive code. Some users may being working on codebases that are locked into competing/incompatible dependencies, which can make it harder to adapt your code to their situation; the more dependencies you have, the more likely this is to occur. 

Some guidelines:

1. Prefer standard library functions to third-party libraries, even if they're not quite as convenient to use.
    - When updating code samples, look for cases where dependencies can be eliminated because the standard library has grown to encompass functionality that previously needed a library.
2. Implement your own functions when they're small and not security-sensitive; use libraries for complex or security-sensitive functions.
3. Prefer widely-used, actively maintained libraries.
{% /admonition %}

### 1. Connect and get account(s)

Each step should be numbered and the heading for the step should be an imperative sentence, in sentence case. Beneath the heading should be a sentence or two introducing the action being taken at this stage of the code sample in more detail. The code samples should be in tabs per programming language.

Most code samples need at least one account. The first step should generally cover from the start of the file (including imports) through instantiating a client, connecting to a network, and deriving wallets and/or funding accounts via the faucet.

{% tabs %}

{% tab label="JavaScript" %}
{% code-snippet file="/_code-samples/verify-credential/js/verify_credential.js" language="js" before="// Look up Credential" /%}
{% /tab %}

{% /tabs %}

{% admonition type="info" name="Code snippets and steps" %}
Each "step" of the tutorial should correspond to one code snippet (with tabs by programming language). There can be exceptions, for example if one programming language needs additional code in a separate place to make the same functionality work.
{% /admonition %}

### 2. Next step

Each additional step should directly continue the code sample from the previous step without skipping anything, to the extent possible. If the code snippet calls an API method, link to the relevant reference documentation. If you include the common links file, you can generally do this with an automatic link such as the `[account_info method][]`, which turns into the [account_info method][].

{% tabs %}

{% tab label="JavaScript" %}
{% code-snippet file="/_code-samples/verify-credential/js/verify_credential.js" language="js" from="// Look up Credential" before="// Check if the credential has been accepted" /%}
{% /tab %}

{% /tabs %}

Optionally, you can provide additional text after the code snippet, such as an explanation of the expected output from this step, or details that you should note down for later.

### 3. Additional steps as necessary

Use `{% code-snippet ... %}` tags instead of copy-paste to display the code samples, so that you don't have to manually keep the code in the doc synchronized with changes to the code sample. To facilitate this, use `from=` and `before=` strings based on unique comments in the code.

{% tabs %}

{% tab label="JavaScript" %}
{% code-snippet file="/_code-samples/verify-credential/js/verify_credential.js" language="js" from="// Check if the credential has been accepted" before="// Confirm that the credential is not expired" /%}
{% /tab %}

{% /tabs %}

## See Also

At the end of the tutorial, provide links to additional resources that would be a sensible next step in the learning journey. This could be more tutorials, use cases, or other pages. It's also a good idea to add links here to reference documentation for any API methods, transaction types, and ledger entries used in the tutorial—even though those links should be redundant with links scattered throughout the text of the tutorial.


{% raw-partial file="/docs/_snippets/common-links.md" /%}
