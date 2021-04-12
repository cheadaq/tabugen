// This file is auto-generated by Tabular v1.4.0, DO NOT EDIT!

#include "AutogenConfig.h"
#include <stddef.h>
#include <assert.h>
#include <memory>
#include <fstream>
#include "Utility/Conv.h"
#include "Utility/StringUtil.h"

using namespace std;

#ifndef ASSERT
#define ASSERT assert
#endif


namespace config {

// parse data object from an csv row
int SoldierPropertyDefine::ParseFromRow(const vector<StringPiece>& row, SoldierPropertyDefine* ptr)
{
    ASSERT(row.size() >= 25);
    ASSERT(ptr != nullptr);
    ptr->Name = parseTextAs<std::string>(row[0]);
    ptr->Level = parseTextAs<int>(row[1]);
    ptr->NameID = parseTextAs<std::string>(row[2]);
    ptr->Description = parseTextAs<std::string>(row[3]);
    ptr->BuildingName = parseTextAs<std::string>(row[4]);
    ptr->BuildingLevel = parseTextAs<uint32_t>(row[5]);
    ptr->RequireSpace = parseTextAs<uint32_t>(row[6]);
    ptr->Volume = parseTextAs<uint32_t>(row[7]);
    ptr->UpgradeTime = parseTextAs<uint32_t>(row[8]);
    ptr->UpgradeMaterialID = parseTextAs<std::string>(row[9]);
    ptr->UpgradeMaterialNum = parseTextAs<int64_t>(row[10]);
    ptr->ConsumeMaterial = parseTextAs<std::string>(row[11]);
    ptr->ConsumeMaterialNum = parseTextAs<int>(row[12]);
    ptr->ConsumeTime = parseTextAs<int>(row[13]);
    ptr->Act = parseTextAs<int>(row[14]);
    ptr->Hp = parseTextAs<int>(row[15]);
    ptr->Hurt = parseTextAs<uint32_t>(row[17]);
    ptr->SearchScope = parseTextAs<int16_t>(row[20]);
    ptr->AtkFrequency = parseTextAs<float>(row[21]);
    ptr->AtkRange = parseTextAs<double>(row[22]);
    ptr->MovingSpeed = parseTextAs<double>(row[23]);
    ptr->EnableBurn = parseTextAs<bool>(row[24]);
    return 0;
}


} // namespace config 
