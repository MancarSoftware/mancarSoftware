<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/mancar-header-static.png" />
  <img src="assets/mancar-header.gif" width="100%" alt="Mancar Software. Designed for people. Engineered for business. Animated geometric M." />
</picture>

# Mancar Software

## Software for the people behind the work.

Mancar Software designs and develops digital products for businesses with real day-to-day needs. We study the work, clarify the experience, and build tools people can rely on—from desktop applications for clinical teams to customer-facing platforms and product catalogues.

The projects below show that approach in practice: focused products shaped around the people, information, and decisions that matter to each business.

# Selected Projects

[01 / OdontoCare](#odontocare) &nbsp; / &nbsp; [02 / VetCare Pro](#vetcare) &nbsp; / &nbsp; [03 / Alma Vet](#almavet) &nbsp; / &nbsp; [04 / Casa Nativa](#casanativa)

## <a id="odontocare"></a>01 / OdontoCare

<a href="https://github.com/MancarSoftware/odonto_care">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/project-odontocare-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/project-odontocare.png" />
  <source media="(max-width: 600px)" srcset="assets/project-odontocare-mobile.gif" />
  <img src="assets/project-odontocare.gif" width="100%" alt="OdontoCare interface tour: patient records, clinical history, and the daily agenda." />
</picture>
</a>

An offline-ready Windows application for managing patient records, appointments, treatments, and payments.

<sub>Interface captured from the repository · Fictional clinical data · Original interface in Spanish</sub>

[View the Still-Image Tour](../docs/PROJECT-GALLERY.md#odontocare) &nbsp; / &nbsp; [Explore the Repository →](https://github.com/MancarSoftware/odonto_care)

**Designed For:** dental clinics managing clinical and administrative work in one place.

**Core Functionality:** patient histories, appointments, odontograms, treatments, payments, inventory, and reporting. The documented workflows also cover user roles, audit records, backups, and restoration.

**Built With:** Electron, React, TypeScript, NestJS, PostgreSQL, and Prisma.

<details>
<summary>Deployment and Engineering Details</summary>

Designed as an installable Windows application with local PostgreSQL storage. The production installer manages the required application services, allowing the clinic to work offline. The repository documents verification procedures for critical workflows, packaging, backup restoration, and installation.

</details>

[Read the User Guide](https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md) · [Review the Release Checklist](https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md)

## <a id="vetcare"></a>02 / VetCare Pro

<a href="https://github.com/MancarSoftware/vetCarePro">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/project-vetcare-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/project-vetcare.png" />
  <source media="(max-width: 600px)" srcset="assets/project-vetcare-mobile.gif" />
  <img src="assets/project-vetcare.gif" width="100%" alt="VetCare Pro interface tour: patients, clinical history, and the record entry form." />
</picture>
</a>

Veterinary practice software for standalone and local network environments, with clinical records, scheduling, and payments accessible across the clinic.

<sub>Interface captured from the repository · Fictional clinical data · Original interface in Spanish</sub>

[View the Still-Image Tour](../docs/PROJECT-GALLERY.md#vetcare-pro) &nbsp; / &nbsp; [Explore the Repository →](https://github.com/MancarSoftware/vetCarePro)

**Designed For:** veterinary teams working from a single computer or across several computers in the same clinic.

**Core Functionality:** patient records, clinical histories, appointments, vaccinations, treatments, images, and payments. Local network support allows reception, veterinary staff, and the payment desk to access the same system.

**Built With:** Electron, Node.js, and PostgreSQL.

<details>
<summary>Deployment and Engineering Details</summary>

Supports standalone, LAN server, and LAN client modes on Windows. One computer hosts the local services and data, while the others connect through the clinic's network. This local workflow does not require internet access. The repository includes guidance for installation, network configuration, and backups.

</details>

[Review the LAN Test Plan](https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md) · [Read the Setup Guide](https://github.com/MancarSoftware/vetCarePro#readme)

## <a id="almavet"></a>03 / Alma Vet

<a href="https://github.com/MancarSoftware/veterinaria">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/project-almavet-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/project-almavet.png" />
  <source media="(max-width: 600px)" srcset="assets/project-almavet-mobile.gif" />
  <img src="assets/project-almavet.gif" width="100%" alt="Alma Vet interface tour: the clinic homepage, service discovery, and appointment request form." />
</picture>
</a>

A veterinary clinic website that guides pet owners from service discovery to a structured appointment request.

<sub>Interface captured from the repository · Repository demo content · Original interface in Spanish</sub>

[View the Still-Image Tour](../docs/PROJECT-GALLERY.md#alma-vet) &nbsp; / &nbsp; [Explore the Repository →](https://github.com/MancarSoftware/veterinaria)

**Designed For:** the Alma Vet clinic and pet owners requesting care.

**Core Functionality:** service discovery and structured appointment requests, supported by server-side validation, bot protection, persistent request storage, and email notifications. Each request is submitted for review and does not automatically confirm an appointment.

**Built With:** React, Supabase, PostgreSQL, Cloudflare Turnstile, and Resend.

[Read the Architecture and Setup Guide](https://github.com/MancarSoftware/veterinaria#readme)

## <a id="casanativa"></a>04 / Casa Nativa

<a href="https://github.com/MancarSoftware/muebleria">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/project-casanativa-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/project-casanativa.png" />
  <source media="(max-width: 600px)" srcset="assets/project-casanativa-mobile.gif" />
  <img src="assets/project-casanativa.gif" width="100%" alt="Casa Nativa interface tour: the storefront, furniture catalog, product details, and a saved selection." />
</picture>
</a>

A furniture retail website with an editable catalog, color variants, and structured customer inquiry workflows.

<sub>Interface captured from the repository · Repository demo content · Original interface in Spanish</sub>

[View the Still-Image Tour](../docs/PROJECT-GALLERY.md#casa-nativa) &nbsp; / &nbsp; [Explore the Repository →](https://github.com/MancarSoftware/muebleria)

**Designed For:** Casa Nativa and customers exploring furniture for their homes.

**Core Functionality:** a furniture catalog with product photography and color variants, an administration area for publishing products, and tools for space proposals and customer inquiries.

**Built With:** React, TypeScript, Vite, and Supabase.

[Read the Catalog and Administration Guide](https://github.com/MancarSoftware/muebleria#readme)

<sub>MANCAR SOFTWARE</sub>
