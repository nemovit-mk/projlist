<template>
    <div id="DD">
        <v-form>
            <v-container>
        <v-col cols="12">
            <v-autocomplete
                    v-model="select"
                    :loading="loading"
                    :disabled="isUpdating"
                    :items="states"
                    filled
                    chips
                    color="blue-grey lighten-2"
                    :label="$t('chousePump')"
                    multiple
            >
                <template v-slot:selection="data">
                    <v-chip
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            close
                            @click="data.select"
                            @click:close="remove(data.item)"
                    >
<!--                        <v-avatar left>-->
<!--                            <v-img :src="data.item.avatar"></v-img>-->
<!--                        </v-avatar>-->
                        {{ data.item }}
                    </v-chip>
                </template>
                <template v-slot:item="data">
                    <template v-if="typeof data.item !== 'object'">
                        <v-list-item-content v-text="data.item"></v-list-item-content>
                    </template>
                    <template v-else>
<!--                        <v-list-item-avatar>-->
<!--                            <img :src="data.item.avatar">-->
<!--                        </v-list-item-avatar>-->
                        <v-list-item-content>
                            <v-list-item-title v-html="data.item"></v-list-item-title>
<!--                            <v-list-item-subtitle v-html="data.item.group"></v-list-item-subtitle>-->
                        </v-list-item-content>
                    </template>
                </template>
            </v-autocomplete>
        </v-col>
            </v-container>
        </v-form>
    </div>
</template>

<script>
    export default {
        name: "DropDown",
        // vuetify: new Vuetify(),
        data () {
            return {
                loading: false,
                isUpdating: false,
                items: [],
                search: null,
                select: null,
                states: ["erst", "zwei", "drei"],
            };
        },
        props: {
            setDescriptions: {}
        },
        watch: {
            // search (val) {
            //   val && val !== this.select && this.querySelections(val);
            //   console.log(this.select);
            //   console.log(this.search)
            // },
            select(val) {
                console.log(val);
                this.sendSelectedIds(val)
            },
            setDescriptions(val) {
                if (Array.isArray(val)) {
                    this.states.length = 0;
                    val.forEach(item => this.states.push(item.designation));
                }
                // console.log(val)
                // this.setItems (val);
            }
        },
        methods: {
            // setItems(items) {
            //     this.states = items;
            // },
            // querySelections (v) {
            //   this.loading = true
            //   // Simulated ajax query
            //   setTimeout(() => {
            //     this.items = this.states.filter(e => {
            //       return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
            //     })
            //     this.loading = false
            //   }, 500)
            // },
            sendSelectedIds () {
                this.$emit('selectedIds', "test");//, idsList);
            },
            remove (item) {
                const index = this.select.indexOf(item)
                if (index >= 0) this.select.splice(index, 1)
            }
        }
 }
</script>

<style scoped>

</style>