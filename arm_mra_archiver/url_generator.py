import itertools
from typing import Final

from .url_bundle import URLBundle

# From ~2019-02-02
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/ARMv85A-SysReg-00bet9.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/A64_v85A_ISA_xml_00bet9.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/AArch32_v85A_ISA_xml_00bet9.tar.gz

# From ~2019-12-19
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/SysReg_xml_v86A-2019-12.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/A64_ISA_xml_v86A-2019-12.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2019-12/AArch32_ISA_xml_v86A-2019-12.tar.gz

# From 2024-02-08
# https://developer.arm.com/-/media/developer/products/architecture/armv9-a-architecture/2023-12/SysReg_xml_A_profile-2023-12.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv9-a-architecture/2023-12/ISA_A64_xml_A_profile-2023-12.tar.gz
# https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/2023-12/ISA_AArch32_xml_A_profile-2023-12.tar.gz

v8_v1_url_template: Final = "https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/{v8_v1_type_ver}00bet{v8_beta_ver}.tar.gz"
v8_v2_url_template: Final = "https://developer.arm.com/-/media/developer/products/architecture/armv8-a-architecture/{v8_v2_date}/{v8_v2_type}_xml_v{v8_v2_major_ver}A-{v8_v2_date}.tar.gz"
v9_url_template: Final = "https://developer.arm.com/-/media/developer/products/architecture/armv9-a-architecture/{v9_date}/{v9_type}_xml_A_profile-{v9_date}.tar.gz"

v8_v2_dates: Final = tuple(
    [f"{y:04}-{m:02}" for y, m in itertools.product(range(2015, 2023), range(1, 13))]
)
v9_dates: Final = tuple(
    [f"{y:04}-{m:02}" for y, m in itertools.product(range(2019, 2025), range(1, 13))]
)
v8_v2_v9_types: Final = ("SysReg", "A64_ISA", "AArch32_ISA")

v8_v1_major_vers: Final = tuple([f"{v8_ver:02}" for v8_ver in range(80, 86)])
v8_v2_major_vers: Final = tuple([f"{v8_ver:02}" for v8_ver in range(86, 90)])
v8_v1_beta_vers: Final = tuple([str(v8_beta_ver) for v8_beta_ver in range(15)])

v8_v1_major_ver_beta_ver_pairs: Final = tuple(
    [
        (v8_v1_major_ver, v8_v1_beta_ver)
        for v8_v1_major_ver, v8_v1_beta_ver in itertools.product(
            v8_v1_major_vers, v8_v1_beta_vers
        )
    ]
)
v8_v1_sysreg_urls: Final = tuple(
    [
        v8_v1_url_template.format(
            v8_v1_type_ver=f"ARMv{v8_v1_major_ver}A-SysReg-",
            v8_beta_ver=v8_beta_ver,
        )
        for v8_v1_major_ver, v8_beta_ver in itertools.product(
            v8_v1_major_vers, v8_v1_beta_vers
        )
    ]
)
v8_v1_a64_urls: Final = tuple(
    [
        v8_v1_url_template.format(
            v8_v1_type_ver=f"A64_v{v8_v1_major_ver}A_ISA_xml_",
            v8_beta_ver=v8_beta_ver,
        )
        for v8_v1_major_ver, v8_beta_ver in itertools.product(
            v8_v1_major_vers, v8_v1_beta_vers
        )
    ]
)
v8_v1_a32_urls: Final = tuple(
    [
        v8_v1_url_template.format(
            v8_v1_type_ver=f"AArch32_v{v8_v1_major_ver}A_ISA_xml_",
            v8_beta_ver=v8_beta_ver,
        )
        for v8_v1_major_ver, v8_beta_ver in itertools.product(
            v8_v1_major_vers, v8_v1_beta_vers
        )
    ]
)

assert (
    len(v8_v1_major_ver_beta_ver_pairs)
    == len(v8_v1_sysreg_urls)
    == len(v8_v1_a64_urls)
    == len(v8_v1_a32_urls)
)


v8_v2_major_ver_date_pairs: Final = tuple(
    [
        (v8_v2_major_ver, v8_v2_date)
        for v8_v2_major_ver, v8_v2_date in itertools.product(
            v8_v2_major_vers, v8_v2_dates
        )
    ]
)
v8_v2_sysreg_urls: Final = tuple(
    [
        v8_v2_url_template.format(
            v8_v2_type="SysReg",
            v8_v2_major_ver=v8_v2_major_ver,
            v8_v2_date=v8_v2_date,
        )
        for v8_v2_major_ver, v8_v2_date in itertools.product(
            v8_v2_major_vers, v8_v2_dates
        )
    ]
)
v8_v2_a64_urls: Final = tuple(
    [
        v8_v2_url_template.format(
            v8_v2_type="A64_ISA",
            v8_v2_major_ver=v8_v2_major_ver,
            v8_v2_date=v8_v2_date,
        )
        for v8_v2_major_ver, v8_v2_date in itertools.product(
            v8_v2_major_vers, v8_v2_dates
        )
    ]
)
v8_v2_a32_urls: Final = tuple(
    [
        v8_v2_url_template.format(
            v8_v2_type="AArch32_ISA",
            v8_v2_major_ver=v8_v2_major_ver,
            v8_v2_date=v8_v2_date,
        )
        for v8_v2_major_ver, v8_v2_date in itertools.product(
            v8_v2_major_vers, v8_v2_dates
        )
    ]
)

assert (
    len(v8_v2_major_ver_date_pairs)
    == len(v8_v2_sysreg_urls)
    == len(v8_v2_a64_urls)
    == len(v8_v2_a32_urls)
)

v9_sysreg_urls: Final = tuple(
    [v9_url_template.format(v9_type="SysReg", v9_date=v9_date) for v9_date in v9_dates]
)
v9_a64_urls: Final = tuple(
    [v9_url_template.format(v9_type="A64_ISA", v9_date=v9_date) for v9_date in v9_dates]
)
v9_a32_urls: Final = tuple(
    [
        v9_url_template.format(v9_type="AArch32_ISA", v9_date=v9_date)
        for v9_date in v9_dates
    ]
)

assert len(v9_dates) == len(v9_sysreg_urls) == len(v9_a64_urls) == len(v9_a32_urls)


def generate_url_bundles() -> tuple[URLBundle, ...]:
    url_bundles: list[URLBundle] = []
    for i in range(len(v8_v1_major_ver_beta_ver_pairs)):
        v8_v1_major_ver, v8_v1_beta_ver = v8_v1_major_ver_beta_ver_pairs[i]
        v8_v1_sysreg_url = v8_v1_sysreg_urls[i]
        v8_v1_a64_url = v8_v1_a64_urls[i]
        v8_v1_a32_url = v8_v1_a32_urls[i]
        url_bundles.append(
            URLBundle(
                v8_v1_sysreg_url,
                v8_v1_a64_url,
                v8_v1_a32_url,
                v8_major_version=v8_v1_major_ver,
                v8_beta_version=v8_v1_beta_ver,
            )
        )
    for i in range(len(v8_v2_major_ver_date_pairs)):
        v8_v2_major_ver, v8_v2_date = v8_v2_major_ver_date_pairs[i]
        v8_v2_sysreg_url = v8_v2_sysreg_urls[i]
        v8_v2_a64_url = v8_v2_a64_urls[i]
        v8_v2_a32_url = v8_v2_a32_urls[i]
        url_bundles.append(
            URLBundle(
                v8_v2_sysreg_url,
                v8_v2_a64_url,
                v8_v2_a32_url,
                v8_major_version=v8_v2_major_ver,
                v8_date=v8_v2_date,
            )
        )
    for i in range(len(v9_dates)):
        v9_date = v9_dates[i]
        v9_sysreg_url = v9_sysreg_urls[i]
        v9_a64_url = v9_a64_urls[i]
        v9_a32_url = v9_a32_urls[i]
        url_bundles.append(
            URLBundle(v9_sysreg_url, v9_a64_url, v9_a32_url, v9_date=v9_date)
        )
    return tuple(url_bundles)
