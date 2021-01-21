<template>
  <div id="app">
          <v-app id="inspire">
    <DropDown :setDescriptions="design"  @selectedIds="getPumpsWithIds"/>
    <DataTable :setPumps="pumps"  @selectedIds="getCurvesWithPumpsList"/>
    <Graph chartID="erstChart" title="Chart" xKey="x" yKey="y" :data="curves" />
          </v-app>
  </div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import DropDown from '@/components/DropDown'
import DataTable from "@/components/Table"
import Graph from "@/components/Graph"
import axios from 'axios';

export default {
  name: 'App',
  data() {
      return {
          design: {},
          pumps: {},
          curves: { curves: [ [
                  {x: 1.3,
                      y: 1.5},
                  {x: 2.5,
                      y: 2.1},
                  {x: 3.0,
                      y: 4}  ],
                  [
                  {x: 1.0,
                      y: 0.5},
                  {x: 2.3,
                      y: 1.7},
                  {x: 4.1,
                      y: 3.54} ]
          ],
          labels: {
              xAxisLable: "flow",
              yAxisLable: "head"
          }},
          errors: null
      }
  },
  methods: {
    getPumpsWithIds(idsList){
      console.log("ids list", idsList);
        axios.get(`https://nemovit.free.beeceptor.com/pumpsList`)
            .then(response => {
                // JSON responses are automatically parsed.
                this.pumps = response.data.pumps;
            })
            .catch(e => {
                this.errors.push(e)
            })
    },
    getCurvesWithPumpsList(pumpsIds){
        console.log("curves", pumpsIds);
        axios.get(`https://nemovit.free.beeceptor.com/curves`)
            .then(response => {
                // JSON responses are automatically parsed.
                this.curves = response.data;
            })
            .catch(e => {
                this.errors.push(e)
            })
    },
    getDescriptionsList(){
        axios.get(`https://nemovit.free.beeceptor.com/designList`)
            .then(response => {
                // JSON responses are automatically parsed.
                this.design = response.data.designations;
            })
            .catch(e => {
                this.errors.push(e)
            })
    }
  },
  created: function(){
        this.getDescriptionsList()
  },
  components: {
    // HelloWorld,
      DropDown,
      DataTable,
      Graph
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
