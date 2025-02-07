# DevSecOps Induction

## 1. Getting Started

The Learning Journey (<https://taggartinstitute.org/p/the-learning-journey>) is an excellent starting point for how to self teach using resources like those below.

Note: Timeline estimates assume 5-10 hours of study per week alongside regular work duties. Progress may vary based on prior experience and available study time.

### 1.1. Useful tools

Development Environment

- Whiteboard/Diagrams <https://excalidraw.com/> (can import/edit mermaid diagrams)
- Github <https://docs.github.com/en/codespaces/getting-started/quickstart>

Kubernetes (CNCF) Tools

- Skaffold <https://skaffold.dev/docs/quickstart/>
- Minikube <https://kubernetes.io/docs/tutorials/hello-minikube/>
- Talos Linux <https://www.talos.dev/v1.8/introduction/getting-started/>

Infrastructure as Code

- Terraform tutorial <https://developer.hashicorp.com/terraform/tutorials/configuration-language>
- AWS IaC <https://developer.hashicorp.com/terraform/tutorials/aws-get-started>
- Azure IaC <https://developer.hashicorp.com/terraform/tutorials/azure-get-started>

## 2. Free Training Resources

These are our recommended resources for building core technical skillsets.

### 2.1. Cloud Native Fundamentals (4-6 weeks)

**👉 New Team Members Start Here!**

The below links will get you across the cloud native methodology to build, test and deliver infrastructure and software. These skills apply to the subsequent infrastructure operation and development guidance sections.

- [GitLab Basics: Start Using Git:](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html) Learn how to set up Git, clone repositories, and work with branches using GitLab. GitLab Basics: Start Using Git
- [GitHub Codespaces: Using Source Control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace): Perform all Git actions directly within your codespace, including committing changes, creating branches, and raising pull requests.
- [GitHub Actions: Writing Workflows Quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart): A quickstart guide to creating workflows that automate your build, test, and deployment pipeline using GitHub Actions.
- [Ansible YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html): An overview of correct YAML syntax used in Ansible playbooks, including lists, dictionaries, and more.
- [Terraform Configuration Syntax](https://www.terraform.io/docs/configuration/syntax.html): Detailed description of the syntax used in Terraform configuration files, including arguments and blocks.
    - [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs): Use the Amazon Web Services (AWS) provider to interact with the many resources supported by AWS.
    - [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest): The Azure Provider can be used to configure infrastructure in Microsoft Azure using the Azure Resource Manager API's.
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/): A tutorial providing a walkthrough of the basics of Kubernetes workload orchestration.
- [Nine Key Cloud Security Concentrations & SWAT Checklist](https://www.sans.org/posters/nine-key-cloud-security-concentrations-swat-checklist/): A set of best practices for cloud security, broken down by AWS, Azure, and GCP, to help create more secure applications.

### 2.2. Cloud Platform Essentials (2-3 weeks)

These are intro courses and security overviews of the major AWS and Azure platforms (as they use a lot of cloud specific nomenclature it's worth getting across).

#### AWS Resources

- [AWS Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/courses/134/aws-cloud-practitioner-essentials)
- [AWS Security Fundamentals Second Edition](https://explore.skillbuilder.aws/learn/courses/48/aws-security-fundamentals)

#### Azure Resources

- [Microsoft Azure Fundamentals](https://learn.microsoft.com/en-us/training/courses/az-900t00)
- [Microsoft Security Academy](https://microsoft.github.io/PartnerResources/skilling/microsoft-security-academy/start)

### 2.3. Development Paths

Understanding the [OWASP Projects](https://owasp.org/projects/) focused on Secure Development Life Cycle’s (SDLC) will help in getting across the common security capabilities platforms and software should generally have. The below **Data Integration** and **Frontend Frameworks** all are typically secure by default, however the way they are deployed can significantly change their risk profile. For production or high risk environments it’s always best to review the operational procedures against the 2 above standards.

#### Backend Development (4-6 weeks)

Expected outcomes: Basic programming skills, understanding of software design principles and secure development practices

For backends, using a modern API framework like [Huma](https://huma.rocks/why/) ([Your First API tutorial](https://huma.rocks/tutorial/your-first-api/)) is strongly recommended. There is a great video series on Golang as well below:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=fpNruzeYKKF1woJZ&amp;list=PLoILbKo9rG3skRCj37Kn5Zj803hhiuRK6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### Software and code security

- [Safestack intro course](https://safestack.io/free-application-security-program/)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) for software executing on servers (such as Websites and API’s) - default to ASVS Level 2
- [OWASP Mobile ASVS](https://mas.owasp.org/MASVS/) for software executing on clients (such as Mobile Applications) - default to MAS-L2
- Testing & QA - Scan for vulnerabilities and configuration/secret issues with [Trivy](https://aquasecurity.github.io/trivy/), [Prowler](https://github.com/prowler-cloud/prowler) and [checkov](https://github.com/bridgecrewio/checkov)
- Testing & QA - Test websites with [playwright](https://playwright.dev/) and APIs with [Hurl](https://github.com/Orange-OpenSource/hurl) or [Grafana K6](https://github.com/grafana/k6).

#### Data Integration (2-3 weeks each)

Expected outcomes: Understanding how to ingest/manage data with Python and SQL and generate reports with Markdown

Start with building a web app using [evidence.dev](https://docs.evidence.dev/build-your-first-app/) (that makes it easy to generate slick [Apache ECharts](https://echarts.apache.org/en/cheat-sheet.html) visuals). Once you have the basics of how to collate and view data with SQL, then dive into the [SQLMesh CLI quickstart](https://sqlmesh.readthedocs.io/en/stable/quickstart/cli/) to understand how SQL (and python) can be used to transform data at scale. The large number of [execution engines](https://sqlmesh.readthedocs.io/en/stable/integrations/overview/) SQLMesh can use in addition to the [DuckDB Friendly SQL](https://duckdb.org/docs/sql/dialect/friendly_sql.html) its in memory processing can do should make almost any data activities easy to model, test and execute.

Massive datasets should use approaches like [incremental by time range](https://sqlmesh.readthedocs.io/en/stable/guides/incremental_time/) which enable only loading relevant chunks of data as needed. Using the [Athena](https://sqlmesh.readthedocs.io/en/stable/integrations/engines/athena/) execution engine across [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) makes it straightforward to run a managed [Apache Iceberg](https://iceberg.apache.org/) data lake that is suitable for petabyte scale datasets.

Some reporting requirements lead to static / document style reports, in which case [Quarto](https://quarto.org/docs/get-started/hello/jupyter.html) is an excellent open-source scientific and technical publishing system, that supports [Hugo markdown](https://quarto.org/docs/output-formats/hugo.html) for simple documents and [Typst](https://quarto.org/docs/output-formats/typst.html) for advanced typesetting.

For more details on the languages used by the above tools, see below:

- [DuckDB SQL Introduction](https://duckdb.org/docs/sql/introduction.html)
- [Python by example](https://third-bit.com/sdxpy/)
- [Hands-On Programming with R](https://rstudio-education.github.io/hopr/)

#### Frontend frameworks (1-2 weeks each)

- [JavaScript](https://third-bit.com/sdxjs/) (understand JS basics)

The below frameworks are all focused on having simple, minimal code easy for small teams to maintain.

- [Streamlit](https://edit.share.stlite.net) in browser python prototypes can be used for fast prototypes in python that compiles to browser.
- [Hugo](https://gohugo.io/) and [Zola](https://www.getzola.org) are fast simple static site generators.
- [Astro](https://astro.build) is extensible with Javascript/Typescript.
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) is extensible with Python/Jinja.

## 3. Paid Certifications (2-3 months)

The SANS courses / certifications are the hardest (at least 50-100hrs study effort per cert) but most in depth:

- [SANS SEC540: Cloud Security and DevSecOps Automation](https://www.sans.org/cyber-security-courses/cloud-security-devsecops-automation/) - Operations Focus
- [SANS SEC522: Application Security: Securing Web Applications, APIs, and Microservices](https://www.sans.org/cyber-security-courses/application-security-securing-web-apps-api-microservices/) - Development Focus

Otherwise the lower cost certs below are all a fair bit shorter while also being high quality:

- [Linux Foundation Certified Kubernetes Administrator (CKA) + Certified Kubernetes Application Developer (CKAD) + Certified Kubernetes Security Specialist (CKS) Exam Bundle](https://training.linuxfoundation.org/training/cka-ckad-cks-exam-bundle/)
- [AWS Certified Solutions Architect - Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [Microsoft Certified: Azure Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/?practice-assessment-type=certification)
