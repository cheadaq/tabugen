# Copyright (C) 2018-present ichenq@outlook.com. All rights reserved.
# Distributed under the terms and conditions of the Apache License.
# See accompanying files LICENSE.

GO_HEAD_TEMPLATE = """// This file is auto-generated by Tabular v%s, DO NOT EDIT!
package %s

import (
	"bytes"
	"encoding/csv"
	"io"
	"log"
	"strings"
)

var (
	_ = io.EOF
	_ = strings.Split
	_ = log.Panicf
	_ = bytes.NewReader
	_ = csv.NewReader
)

"""

GO_HEAD_CONST_TEMPLATE = """
const (
    TAB_CSV_SEP = `%s`		// CSV field delimiter
    TAB_CSV_QUOTE = `%s`	// CSV field quote
    TAB_ARRAY_DELIM = `%s`	// array item delimiter
    TAB_MAP_DELIM1 = `%s`	// map item delimiter
    TAB_MAP_DELIM2 = `%s`	// map key-value delimiter
)

"""

GO_LOAD_METHOD_TEMPLATE = """
func Load%sList(data []byte) ([]*%s, error) {
    var list []*%s
    var r = csv.NewReader(bytes.NewReader(data))
    for i := 0; ; i++ {
        row, err := r.Read()
        if err == io.EOF {
            break
        }
        if err != nil {
            log.Printf("%s: read csv %%v", err)
            return nil, err
        }
        var item %s
        if err := item.ParseFromRow(row); err != nil {
            log.Printf("%s: parse row %%d, %%s, %%v", i+1, row, err)
            return nil, err
        }
        list = append(list, &item)
    }
    return list, nil
}

"""

GO_KV_LOAD_METHOD_TEMPLATE = """
func Load%s(data []byte) (*%s, error) {
    r := csv.NewReader(bytes.NewReader(data))
    rows, err := r.ReadAll()
    if err != nil {
        log.Printf("%s: csv read all, %%v", err)
        return nil, err
    }
    var item %s
    if err := item.ParseFromRows(rows); err != nil {
        log.Printf("%s: parse row %%d, %%v", len(rows), err)
        return nil, err
    }
    return &item, nil
}

"""

GO_HELP_FILE_HEAD_TEMPLATE = """// This file is auto-generated by Tabular v%s, DO NOT EDIT!
package %s
"""

GO_HELP_FILE_TEMPLATE = """
import (
	"fmt"
	"log"
	"math"
	"strconv"
	"strings"
)

// parse int64 number from string
func MustParseInt64(text string) int64 {
	n, err := strconv.ParseInt(text, 10, 64)
	if err != nil {
		log.Panicf("ParseInt64: %s, %v", text, err)
	}
	return n
}

// parse uint64 number from string
func MustParseUnt64(text string) uint64 {
	n, err := strconv.ParseUint(text, 10, 64)
	if err != nil {
		log.Panicf("ParseUnt64: %s, %v", text, err)
	}
	return n
}

// parse int32 number from string
func ParseInt32(text string) (int32, error) {
	n, err := strconv.ParseInt(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxInt32 || n < math.MinInt32 {
		return 0, fmt.Errorf("int32 [%s] out of range", text)
	}
	return int32(n), nil
}

// parse uint32 number from string
func ParseUint32(text string) (uint32, error) {
	n, err := strconv.ParseUint(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxUint32 || n < 0 {
		return 0, fmt.Errorf("uint32 [%s] out of range", text)
	}
	return uint32(n), nil
}

// parse int16 number from string
func ParseInt16(text string) (int16, error) {
	n, err := strconv.ParseInt(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxInt16 || n < math.MinInt16 {
		return 0, fmt.Errorf("int16 [%s] out of range", text)
	}
	return int16(n), nil
}

// parse uint16 number from string
func ParseUint16(text string) (uint16, error) {
	n, err := strconv.ParseUint(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxUint16 || n < 0 {
		return 0, fmt.Errorf("uint16 [%s] out of range", text)
	}
	return uint16(n), nil
}

// parse int8 number from string
func ParseInt8(text string) (int8, error) {
	n, err := strconv.ParseInt(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxInt8 || n < math.MinInt8 {
		return 0, fmt.Errorf("uint8 [%s] out of range", text)
	}
	return int8(n), nil
}

// parse uint8 number from string
func ParseUint8(text string) (uint8, error) {
	n, err := strconv.ParseUint(text, 10, 64)
	if err != nil {
		return 0, err
	}
	if n > math.MaxUint8 || n < 0 {
		return 0, fmt.Errorf("uint8 [%s] out of range", text)
	}
	return uint8(n), nil
}

// parse float64 from string
func ParseFloat64(text string) (float64, error) {
	f, err := strconv.ParseFloat(text, 64)
	if err != nil {
		return 0, err
	}
	if math.IsNaN(f) || math.IsInf(f, 0) {
		return 0, fmt.Errorf("ParseFloat64: [%s] not a number", text)
	}
	return f, nil
}

// parse float32 from string
func ParseFloat32(text string) (float32, error) {
	f, err := strconv.ParseFloat(text, 32)
	if err != nil {
		return 0, err
	}
	if math.IsNaN(f) || math.IsInf(f, 0) {
		return 0, fmt.Errorf("ParseFloat32: [%s] not a number", text)
	}
	if f > math.MaxFloat32 || f < math.SmallestNonzeroFloat32 {
		return 0, fmt.Errorf("uint8 [%s] out of range", text)
	}
	return float32(f), nil
}

// parse boolean value from string
func ParseBool(text string) (bool, error) {
	switch len(text) {
	case 0:
		return false, nil
	case 1:
		if text[0] == '1' || text[0] == 'Y' || text[0] == 'y' {
			return true, nil
		} else if text[0] == '0' || text[0] == 'N' || text[0] == 'n' {
			return false, nil
		}
		return false, fmt.Errorf("ParseBool: cannot parse %s", text)
	case 2:
		if text == "ON" || text == "on" {
			return true, nil
		} else if text == "NO" || text == "no" {
			return false, nil
		}
		return false, fmt.Errorf("ParseBool: cannot parse %s", text)
	case 3:
		if text == "YES" || text == "yes" {
			return true, nil
		} else if text == "OFF" || text == "off" {
			return false, nil
		}
		return false, fmt.Errorf("ParseBool: cannot parse %s", text)
	default:
		return strconv.ParseBool(text)
	}
}

// parse string to number or boolean
func ParseStringAs(typename, value string) (interface{}, error) {
	switch typename {
	case "int":
		n, err := strconv.ParseInt(value, 10, 64)
		return int(n), err
	case "uint":
		n, err := strconv.ParseUint(value, 10, 64)
		return uint(n), err
	case "int32":
		return ParseInt32(value)
	case "uint32":
		return ParseUint32(value)
	case "int64":
		return strconv.ParseInt(value, 10, 64)
	case "uint64":
		return strconv.ParseUint(value, 10, 64)
	case "int16":
		return ParseInt16(value)
	case "uint16":
		return ParseUint16(value)
	case "int8":
		return ParseInt8(value)
	case "uint8":
		return ParseUint8(value)
	case "float32":
		return ParseFloat32(value)
	case "float64":
		return ParseFloat64(value)
	case "bool":
		return ParseBool(value)
	}
	return strings.TrimSpace(value), nil
}

// parse string to numeric value
func MustParseStringAs(typename, value string, posTips interface{}) interface{} {
	v, err := ParseStringAs(typename, value)
	if err != nil {
		log.Panicf("parse value %s to %s : %v, row: %s", value, typename, err, posTips)
	}
	return v
}

"""