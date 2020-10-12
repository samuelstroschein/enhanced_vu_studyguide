<script>
import Button from "smelte/src/components/Button";



const SparqlClient = require('sparql-http-client')
 
const endpointUrl = 'https://dbpedia.org/sparql'
const query = `
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?companyDBPEDIA ?numberEmployee where {
  { ?companyDBPEDIA rdf:type dbo:Company;
                     rdfs:label "Nvidia"@en;
      				dbo:numberOfEmployees ?numberEmployee.} 
  UNION { ?companyDBPEDIA rdf:type dbo:Company;
						rdfs:label "Advanced Micro Devices"@en;
                        dbo:numberOfEmployees ?numberEmployee.} 
} `
 
async function SparQL() {
  const client = new SparqlClient({ endpointUrl })
  const stream = await client.query.select(query)
 
  stream.on('data', row => {
    Object.entries(row).forEach(([key, value]) => {
      console.log(`${key}: ${value.value} (${value.termType})`)
    })
  })
  stream.on('error', err => {
    console.error(err)
  })
}
 
SparQL()

// https://www.npmjs.com/package/sparql-http-client This is the package used for SPARQL
// Above code does return back shit from SPARQL, which is great but I can't get it to only run when clicking the Start Search Button. 
</script>

<div class="flex justify-center">
    <Button color="blue" on:click={SparQL}>Start Search</Button>
</div>