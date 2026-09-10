<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="profile/assets/mancar-header-static.png" />
  <img src="profile/assets/mancar-header.gif" width="100%" alt="Mancar Software. Designed for people. Engineered for business. Animated geometric M." />
</picture>

<p><strong>Websites, applications, and business systems for the way you work.</strong><br>We bring product design and software engineering together for businesses and SMEs.</p>

A customer deciding to get in touch. A receptionist finding the next appointment. A team keeping its records in order. We design around these everyday moments, connecting a clear public presence with useful software behind the scenes.

[Capabilities](#capabilities) &nbsp; / &nbsp; [Selected work](#selected-work) &nbsp; / &nbsp; [Working together](#working-together) &nbsp; / &nbsp; [Let’s talk](https://www.instagram.com/mancarsoftware/)

<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/mancar-capabilities-mobile.svg" />
  <img src="profile/assets/mancar-capabilities.svg" width="100%" alt="What we build: web experiences — websites, landing pages and catalogs; business software — desktop systems and local networks; custom applications — interfaces, services and databases." />
</picture>

## Capabilities

**Build your digital presence.** Corporate websites, landing pages, and catalogs that explain your services, express your identity, and guide visitors toward an inquiry. Responsive layouts and clear content help people find what matters on any screen.

**Bring your operations together.** Business applications for records, appointments, inventory, payments, and reporting. We shape the workflow around the people doing the work, with roles and access appropriate to each responsibility.

**Create a product around a specific need.** Custom web applications and desktop software that connect interfaces, business logic, and data. The scope can include authentication, APIs, and integrations with existing tools.

<details>
<summary>Where the software runs</summary>

- **Web:** for products and experiences accessed through a browser.
- **Local desktop:** for work on a dedicated computer, including workflows that need to operate offline.
- **Local network:** for teams sharing a system across computers at the same location.

We choose the setup around connectivity, access, data handling, and maintenance needs. Our featured clinical products demonstrate local and LAN approaches; deployment requirements are defined for each project.

</details>

## Selected work

A closer look at our work for dental practices, veterinary clinics, and local service businesses. Explore the repositories for implementation details and setup documentation.

<a href="https://github.com/MancarSoftware/odonto_care">
<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/project-odontocare-mobile.svg" />
  <img src="profile/assets/project-odontocare.svg" width="100%" alt="OdontoCare — explore the repository." />
</picture>
</a>

Patient records, appointments, treatments, and payments in a Windows application that works offline.

**For:** dental clinics managing clinical and administrative work in one place.

**Inside the product:** patient histories, appointments, odontograms, treatments, payments, inventory, and reporting. Its documented workflows also cover roles, audit records, backups, and restoration.

**Built with:** Electron, React, TypeScript, NestJS, PostgreSQL, and Prisma.

<details>
<summary>Deployment and engineering details</summary>

Designed as an installable Windows application with local PostgreSQL storage. The production installer manages the application services so the clinic can work offline. The repository documents verification for critical workflows, packaging, backup restoration, and installation.

</details>

[Explore OdontoCare →](https://github.com/MancarSoftware/odonto_care)

[Read the user guide](https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md) · [Review the release checklist](https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md)

<a href="https://github.com/MancarSoftware/vetCarePro">
<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/project-vetcare-mobile.svg" />
  <img src="profile/assets/project-vetcare.svg" width="100%" alt="VetCare Pro — explore the repository." />
</picture>
</a>

Veterinary software for a single PC or a connected clinic, with records and payments available over the local network.

**For:** veterinary teams working from one computer or several computers in the same clinic.

**Inside the product:** pet records, clinical histories, appointments, vaccines, treatments, images, and payments. Local network operation lets reception, veterinary staff, and the payment desk work with the shared system.

**Built with:** Electron, Node.js, and PostgreSQL.

<details>
<summary>Deployment and engineering details</summary>

Supports standalone, LAN server, and LAN client modes on Windows. One computer hosts the local services and data; the others connect over the clinic's network. Internet access is not required for this local workflow. The repository includes installation, network configuration, and backup guidance.

</details>

[Explore VetCare Pro →](https://github.com/MancarSoftware/vetCarePro)

[Review the LAN test plan](https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md) · [Read the setup guide](https://github.com/MancarSoftware/vetCarePro#readme)

<a href="https://github.com/MancarSoftware/beauty-business-template">
<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/project-beauty-mobile.svg" />
  <img src="profile/assets/project-beauty.svg" width="100%" alt="Beauty Business — explore the repository." />
</picture>
</a>

<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/beauty-business-preview-mobile.png" />
  <img src="profile/assets/beauty-business-preview.png" width="100%" alt="Actual rendered BarberPro template: dark barbershop imagery, service introduction, and yellow appointment buttons. Demonstration with sample business content." />
</picture>

<sub>Actual interface rendered from the Beauty Business repository. BarberPro is a template demonstration; business details, ratings, and offers shown are sample content.</sub>

Adaptable websites for barbershops, salons, and spas, with service listings, galleries, and contact sections.

**For:** barbershops, salons, spas, and beauty businesses presenting their services online.

**Inside the project:** service listings, galleries, packages, and contact sections. Content and business data are organized so the website can be adapted to a different service business without rewriting its interface.

**Built with:** React, JavaScript, Vite, and Tailwind CSS.

<details>
<summary>Design and implementation details</summary>

A reusable website foundation with shared components and centralized business content. The project separates presentation from business-specific data, making it easier to change the offer, imagery, and contact information together.

</details>

[Explore Beauty Business →](https://github.com/MancarSoftware/beauty-business-template)

[Inspect the example’s content structure](https://github.com/MancarSoftware/beauty-business-template/blob/5ae0e3bd3186fa6aee8a703a0cd4b6e359537018/src/data/barberiaData.js)

<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/mancar-approach-mobile.svg" />
  <img src="profile/assets/mancar-approach.svg" width="100%" alt="How we build: understand the real workflow; design for clear everyday use; engineer foundations that evolve." />
</picture>

## Working together

**01 / Define the right scope.** Start with the business goal, the users, and the current workflow. Identify the essential features, constraints, integrations, and what a successful first release needs to achieve.

**02 / Make the experience concrete.** Organize the information and map the important user journeys. Establish a visual direction and review the key screens before expanding the implementation.

**03 / Build in useful increments.** Develop around complete workflows, with clear responsibilities in the code and feedback as the product takes shape. Add complexity when the requirements justify it.

**04 / Validate and prepare delivery.** Check the critical paths, permissions, error handling, and deployment setup. Define the installation and operating documentation needed for the agreed environment.

<details>
<summary>What we plan for beyond the first release</summary>

- **Maintainability:** readable code, clear boundaries, and documented setup.
- **Usability:** accessible interaction, useful feedback, and recovery from errors.
- **Data protection:** input validation, appropriate access controls, and backup planning where relevant.
- **Performance:** attention to real loading, rendering, and data-access bottlenecks.
- **Handover:** installation, configuration, and operating instructions appropriate to the product.

Hosting, ongoing maintenance, future features, and support arrangements belong in the project scope so expectations are clear from the beginning.

</details>

## Decisions that shape the product

**Connectivity is a requirement.** A public website and a clinic's internal system have different needs. We consider where people work, how they connect, and what must remain available when the internet is down.

**Recovery belongs in the plan.** Installation, backups, updates, and operating instructions affect the usefulness of a business system as much as its screens. The clinical project guides above make these concerns concrete.

**Design continues after the first screen.** Navigation, validation, empty states, and feedback deserve the same attention as the opening impression. The aim is a product people can understand and keep using.

## Our toolkit

A focused ecosystem reflected in the projects above. We choose tools around the product’s needs, deployment environment, and long-term maintenance.

**Interface** &nbsp; React · TypeScript · JavaScript · Tailwind CSS<br>
**Application** &nbsp; Node.js · NestJS · Electron<br>
**Foundation** &nbsp; PostgreSQL · Prisma · Docker · Git

## Before we start

<details>
<summary>Do I need a complete specification?</summary>

Start with the problem, the people affected, and an example of how the work happens today. Screenshots, spreadsheets, or a description of your existing process can help shape the first scope.

</details>

<details>
<summary>Can the software work with our existing tools?</summary>

We first review the available APIs, data formats, access permissions, and workflow. Integration and data migration need to be scoped around what those systems actually support.

</details>

<details>
<summary>What determines the timeline and budget?</summary>

The critical workflows, design scope, integrations, data migration, and deployment environment. Sharing a target date and budget range helps define a realistic first release and what can follow later.

</details>

<details>
<summary>What happens after delivery?</summary>

Maintenance, hosting, updates, and support responsibilities are defined in the project scope. They should be clear before development starts, alongside the documentation and handover requirements.

</details>

<a href="https://www.instagram.com/mancarsoftware/">
<picture>
  <source media="(max-width: 600px)" srcset="profile/assets/mancar-contact-mobile.svg" />
  <img src="profile/assets/mancar-contact.svg" width="100%" alt="What could work better? Talk to Mancar Software about your next project on Instagram." />
</picture>
</a>

## Start with the problem

Tell us what your business does, who will use the software, and what is difficult today. A rough idea is enough to start the conversation.

Helpful details include the features you have in mind, existing tools or data, whether the product needs to work locally or online, and your target timeline and budget range.

**For developers and collaborators:** explore the repositories for stack choices, setup instructions, and implementation details. For a collaboration proposal, introduce your area of expertise and the project you would like to discuss.

[Discuss a project on Instagram →](https://www.instagram.com/mancarsoftware/) &nbsp; / &nbsp; [Browse our repositories](https://github.com/MancarSoftware?tab=repositories)

<sub>MANCAR SOFTWARE · Designed for people. Engineered for business.</sub>
