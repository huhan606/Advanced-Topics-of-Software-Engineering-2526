# Advanced Topics of Software Engineering: CI/CD

Welcome to the Python CI/CD Tutorial! This guide will walk you through enhancing a simple `Calculator` class, setting up a Continuous Integration and Continuous Deployment (CI/CD) pipeline on Github Actions, and ensuring your code meets high-quality standards through automated testing and code coverage.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Tutorial Steps](#tutorial-steps)
   1. [1. Clone the Repository](#1-clone-the-repository)
   2. [2. Create a Virtual Environment](#2-create-a-virtual-environment)
   3. [3. Install Requirements](#3-install-requirements)
   4. [4. Run Unit Tests Offline](#4-run-unit-tests-offline)
   5. [5. Fix the Bug in the Code](#5-fix-the-bug-in-the-code)
   6. [6. Push to Your Own Repository](#6-push-to-your-own-repository)
   7. [7. Check CI Results](#7-check-ci-results)
   8. [8. Write Additional Test Cases](#8-write-additional-test-cases)
   9. [9. Push Again and Check Coverage Report](#9-push-again-and-check-coverage-report)
   10. [10. Check the CD YAML File](#10-check-the-cd-yaml-file)
3. [Additional Resources](#additional-resources)
4. [Troubleshooting](#troubleshooting)
5. [Conclusion](#conclusion)

---

## Prerequisites

Before starting the tutorial, ensure you have the following installed on your machine:

* **Git**: Version control system. [Download Git](https://git-scm.com/downloads)
* **Anaconda**: Package and environment management system. [Download Anaconda](https://www.anaconda.com/download)
* **Python 3.8 in anaconda**: Programming language.
* **GitHub Account**: To host your repository and use GitHub Actions for CI/CD.
* **Code Editor**: Such as VS Code, PyCharm, or any preferred editor.

---

## Tutorial Steps

### 1. Clone the Repository

Begin by cloning the tutorial repository to your local machine.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">gh repo clone tum-seai/Advanced-Topics-of-Software-Engineering
cd Advanced-Topics-of-Software-Engineering
</code></div></div></pre>

> **Note:** Replace `your-username` with your GitHub username. Make sure you have forked the repository.
> if you need to you are required to authorize your account when cloning the repo, please choose `SSH` way. (Need to create a new key on GitHub)

### 2. Create a Virtual Environment

Creating a virtual environment helps manage project-specific dependencies. 

Open "Anaconda Prompt":

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">conda create -n myenv python=3.8
</code></div></div></pre>

> **Note:** Replace `myenv` with your own environment name.


Activate the virtual environment:

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">conda activate myenv
</code></div></div></pre>

### 3. Install Requirements

Install the necessary Python packages using `pip`. Ensure you have a `requirements.txt` file in the repository.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install --upgrade pip
pip install -r requirements.txt
</code></div></div></pre>

> **Tip:** If `requirements.txt` is not present, you can create one based on the dependencies used in the project.

### 4. Run Unit Tests Offline

Before making any changes, run the existing unit tests to ensure everything is working correctly.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">coverage run -m pytest
</code></div></div></pre>

You should see output indicating that all tests have passed. If there are any failures, review the test cases and the code to understand the issues.

### 5. Fix the Bug in the Code

For this tutorial, a deliberate bug has been introduced in the `Calculator` class. Your task is to identify and fix it.

### 6. Push to Your Own Repository

To implement CI/CD, you need to work on your own fork of the repository.

1. **Commit and Push Your Changes:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git add calculator.py
   git commit -m "Fix bug"
   git push origin main
   </code></div></div></pre>

> **Note:** Replace `your-username` with your GitHub username.

### 7. Check CI Results

After pushing your changes, GitHub Actions will automatically trigger the CI workflow.

1. **Navigate to Your Repository on GitHub.**
2. **Go to the "Actions" Tab:**
   * Here, you can see the status of your CI workflows.
   * Ensure that all tests pass successfully.

> **Tip:** If the CI fails, review the error logs provided in the Actions tab to debug and fix the issues.

### 8. Write Additional Test Cases

To achieve over 90% code coverage, you need to write more comprehensive test cases.

1. **Open the Test File**
2. **Add Test Cases for Advanced Functions:**

   * Ensure that all methods in the `Calculator` class are tested, including edge cases.
3. **Run Tests Locally to Ensure They Pass:**

   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">coverage run -m pytest
   </code></div></div></pre>
4. **Check Code Coverage:**
   Ensure that your test coverage is above 90%. You can use `coverage.py` to check this.

   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">
   coverage report
   coverage html  # Generates an HTML report
   </code></div></div></pre>

### 9. Push Again and Check Coverage Report

After writing additional tests:

1. **Commit Your Test Cases:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git add tests/test_calculator.py
   git commit -m "Add additional test cases for Calculator class"
   </code></div></div></pre>
2. **Push to GitHub:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git push origin main
   </code></div></div></pre>
3. **Verify Coverage Report:**
   * GitHub Actions should automatically run the CI workflow, including code coverage checks.
   * Navigate to the "Actions" tab to ensure that the coverage report is uploaded successfully.

### 10. Check the CD YAML File

Review the Continuous Deployment (CD) configuration to understand the deployment pipeline.

1. **Locate the CD Workflow File**
2. **Review the YAML Configuration**
3. **Understand Each Step**

## Conclusion

Congratulations! By completing this tutorial, you've:

* Enhanced a Python `Calculator` class with advanced features.
* Set up a virtual environment and managed dependencies.
* Implemented unit tests and achieved high code coverage.
* Configured a CI/CD pipeline using GitHub Actions to automate testing and deployment.

These skills are essential for modern software development, ensuring code quality, reliability, and streamlined deployment processes. Happy coding!
