<template>
    <div class="Table">
            <v-data-table
                    v-model="selected"
                    :headers="headers"
                    :items="pumps"
                    item-key="id"
                    show-select
                    class="elevation-1"
            >

            </v-data-table>
    </div>
</template>

<script>
    export default {
        name: "DataTable",
        data () {
            return {
                // singleSelect: false,
                selected: [],
                headers: [
                    { text: this.$t('design'),
                        align: 'start',
                        sortable: false,
                        value: 'designation' },
                    { text: this.$t('speed'), value: 'nom_speed' },
                    { text: this.$t('diam'), value: 'L diam' },
                    { text: this.$t('laufrad'), value: 'laufrad' },
                ],
                pumps: [
                ],
            }
        },
        props: {
            setPumps: {}
        },
        watch: {
            selected(val) {
                console.log(val);
                this.sendSelectedPumps(val)
            },
            setPumps(val) {
                if (Array.isArray(val)) {
                    this.pumps.length = 0;
                    val.forEach(item => this.pumps.push(item));
                }
                // console.log(val)
                // this.setItems (val);
            }
        },
        methods: {
            sendSelectedPumps () {
                this.$emit('selectedPumps', "test");//, idsList);
            }
        }
    };
</script>
