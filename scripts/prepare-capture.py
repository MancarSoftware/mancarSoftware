"""Prepare disposable repository clones for interface captures with fictional data.

Usage: python scripts/prepare-capture.py PATH_TO_CLONES
Never run this against production checkouts. No real API or database is used.
"""
from pathlib import Path
import json
import sys

root = Path(sys.argv[1]).resolve()
if root.name != 'mancar-project-evidence':
    raise SystemExit('Use disposable clones in a directory named mancar-project-evidence.')
odo = root / 'odonto_care/apps/desktop'
vet = root / 'vetCarePro/apps/desktop'

def write(path, content):
    path.write_text(content, encoding='utf-8')

def replace(path, old, new):
    source = path.read_text(encoding='utf-8')
    if old not in source:
        raise ValueError(f'Expected source changed: {path}')
    write(path, source.replace(old, new, 1))

user = dict(id='demo-doctor', fullName='Dra. Andrea Demo', email='studio@example.invalid', role='ADMIN')
patients = [dict(id=f'demo-{i}', code=f'DEMO-00{i+1}', firstName=first, lastName=last,
    documentId=None, birthDate='1994-04-12', gender='UNSPECIFIED', phone=None,
    email=f'patient{i+1}@example.invalid', address='Datos ficticios de demostración',
    allergies=None, medicalAlerts=None, createdAt='2026-09-01T12:00:00Z',updatedAt='2026-09-10T12:00:00Z',
    occupation=None, emergencyContactName=None, emergencyContactPhone=None,
    notes='Ficha de ejemplo para la presentación de Mancar Software.',clinicalEntries=[dict(id=f'entry-{i}',
    author=user,title='Evaluación inicial',type='CONSULTATION',notes='Registro ficticio para mostrar el historial clínico.',
    createdAt='2026-09-10T12:00:00Z',updatedAt='2026-09-10T12:00:00Z')])
    for i,(first,last) in enumerate([('Sofía','Ejemplo'),('Mateo','Demo'),('Valentina','Muestra'),('Daniel','Ejemplo')])]
write(odo/'src/capture-fixtures.ts', f'''// Capture-only fictional data; no application presentation components are changed.
const patients = {json.dumps(patients,ensure_ascii=False)};
const user = {json.dumps(user)};
localStorage.setItem('odontocare.accessToken','local-capture');
localStorage.setItem('odontocare.user',JSON.stringify(user));
export async function captureRequest(path: string, options: any = {{}}): Promise<any> {{
  if (options.method && options.method !== 'GET') throw new Error('Read-only capture fixture');
  if (path.startsWith('/patients/')) return patients.find(p=>p.id===path.split('/')[2]) ?? patients[0];
  if (path.startsWith('/patients')) return patients;
  if (path.startsWith('/appointments/doctors')) return [user];
  if (path.startsWith('/appointments')) return patients.map((patient,i)=>{{
    const start=new Date(); start.setHours(9+i,0,0,0);
    return {{id:'appointment-'+i,patient,doctor:user,startsAt:start.toISOString(),
      endsAt:new Date(+start+3600000).toISOString(),status:i%2?'PENDING':'CONFIRMED',
      title:['Evaluación inicial','Control preventivo','Seguimiento','Consulta general'][i],notes:'Demostración',color:null}};
  }});
  return [];
}}
''')
replace(odo/'src/lib/api.ts', 'import { LOCAL_API_DEFAULT_URL }', "import { captureRequest } from '../capture-fixtures';\nimport { LOCAL_API_DEFAULT_URL }")
replace(odo/'src/lib/api.ts', 'const headers: Record<string, string> = {};', 'return captureRequest(path, options);\n  const headers: Record<string, string> = {};')
replace(odo/'src/App.tsx', 'useState<AppSectionId>("dashboard")', 'useState<AppSectionId>("patients")')

owner = dict(id='owner-demo',firstName='Familia',lastName='Demo',phone='—',email='owner@example.invalid',pets=[],_count=dict(pets=3))
pets = [dict(id=f'pet-{i}',ownerId=owner['id'],name=name,species=species,breed=breed,sex='FEMALE' if i==0 else 'MALE',
    birthDate='2022-05-12',approximateAgeMonths=None,weightKg=weight,color=None,photoPath=None,
    status='ACTIVE',notes='Paciente ficticio de demostración',createdAt='2026-09-01T12:00:00Z',updatedAt='2026-09-10T12:00:00Z',owner=owner)
    for i,(name,species,breed,weight) in enumerate([('Luna','Canino','Mestiza',12.4),('Milo','Felino','Europeo',4.2),('Bruno','Canino','Labrador',28)])]
records=[dict(id='record-demo',petId='pet-0',veterinarianId='vet-demo',type='CONSULTATION',occurredAt='2026-09-10T14:00:00Z',
    complaint='Control preventivo de ejemplo',symptoms='Registro ficticio',diagnosis='Evaluación de demostración',
    treatmentPlan='Seguimiento de ejemplo. No es una indicación médica.',medications=[],notes='Datos ficticios',nextReviewAt=None,
    createdAt='2026-09-10T14:00:00Z',updatedAt='2026-09-10T14:00:00Z',pet=pets[0],
    veterinarian=dict(id='vet-demo',firstName='Andrea',lastName='Demo'),_count=dict(treatments=0,vaccines=0,dewormings=0,mediaFiles=0))]
permissions=[f'{area}.{action}' for area in ('dashboard','pets','owners','appointments','medical','vaccines','treatments','payments','finance','inventory','reports','users','settings','backups') for action in ('read','manage')]
vetuser=dict(id='vet-demo',firstName='Andrea',lastName='Demo',email='studio@example.invalid',roles=['ADMIN'],permissions=permissions)
write(vet/'src/renderer/src/contexts/auth-context.tsx', f'''// Capture-only adapter: original UI, fictional data, no backend writes.
import type {{ReactNode}} from 'react';
const pets={json.dumps(pets,ensure_ascii=False)};
const owners={json.dumps([owner],ensure_ascii=False)};
const records={json.dumps(records,ensure_ascii=False)};
const user={json.dumps(vetuser)};
const page=(items:any[])=>({{items,total:items.length,page:1,pageSize:100,totalPages:1}});
async function request<T>(path:string,options:any={{}}):Promise<T>{{
 if(options.method && options.method!=='GET') throw new Error('Read-only capture fixture');
 if(path.startsWith('/pets')) return page(pets) as T;
 if(path.startsWith('/owners')) return page(owners) as T;
 if(path.startsWith('/medical-records')) return page(records) as T;
 if(path==='/dashboard/summary') return {{generatedAt:new Date().toISOString(),metrics:{{registeredPets:3,appointmentsToday:0,pendingVaccines:0,monthlyIncome:0,monthlyExpenses:0,monthlyNetIncome:0}},agendaToday:[],upcomingVaccines:[],lowStock:[],recentPatients:pets,activeTreatments:[],incomeLastSixMonths:[]}} as T;
 return page([]) as T;
}}
const auth={{user,status:'authenticated',request,requestBlob:async()=>new Blob(),logout:async()=>{{}},login:async()=>{{}},initialize:async()=>{{}}}};
export function useAuth(){{return auth;}}
export function AuthProvider({{children}}:{{children:ReactNode}}){{return <>{{children}}</>;}}
''')
replace(vet/'src/renderer/src/App.tsx', "useState<AppPage>('dashboard')", "useState<AppPage>('pets')")
# The local fixture health endpoint keeps the original runtime indicator consistent.
write(vet/'capture.vite.config.mjs', '''import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'node:path';
export default defineConfig({root:path.resolve('src/renderer'),plugins:[react(),tailwindcss(),{name:'capture-health',configureServer(server){server.middlewares.use('/capture-health',(req,res)=>{res.setHeader('Content-Type','application/json');res.end('{}');});}}],resolve:{alias:{'@':path.resolve('src/renderer/src')}},server:{host:'127.0.0.1',port:4192}});
''')
replace(vet/'src/renderer/src/contexts/runtime-config-context.tsx', "healthUrl: `${import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:4782/api'}/health`,", "healthUrl: '/capture-health',")
for app in (odo,vet/'src/renderer',root/'veterinaria',root/'muebleria'):
    write(app/'capture.html', '''<!doctype html><html><head><meta charset="utf-8"><title>Repository interface capture</title><style>html,body{margin:0;background:#101416}iframe{border:0;width:1440px;height:960px;transform:scale(.65);transform-origin:0 0;display:block}</style></head><body><iframe src="/" title="Project interface"></iframe></body></html>''')
print('Prepared capture adapters in disposable clones. Original interface components preserved.')
