import { select, selectAll, mouse } from 'd3-selection';

import {
    scaleLinear,
    scaleBand,
    scaleTime,
    scaleOrdinal,
    // schemeCategory10,
} from 'd3-scale';

import { axisTop, axisBottom, axisLeft } from 'd3-axis';

import { schemeCategory10 } from 'd3-scale-chromatic';

import { max, min } from "d3-array";

import { line, curveCardinal, curveLinear } from "d3-shape";

import { format } from "d3-format";

export default {
    curveCardinal,
    curveLinear,
    format,
    line,
    max,
    min,
    mouse,
    select,
    selectAll,
    scaleLinear,
    scaleBand,
    scaleTime,
    scaleOrdinal,
    schemeCategory10,
    axisTop,
    axisLeft,
    axisBottom,
};