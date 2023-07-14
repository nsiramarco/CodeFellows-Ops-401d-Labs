#Set Password Requirements length and enable complexity
## Set the desired password policy values
$minimumPasswordLength = 6
$passwordComplexity = $true

## Set the password policy using Group Policy Preferences
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft Services\AdmPwd" -Name "MinimumPasswordLength" -Value $minimumPasswordLength
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft Services\AdmPwd" -Name "PasswordComplexityEnabled" -Value $passwordComplexity

## Refresh Group Policy
gpupdate /force

Write-Host "Password policy updated successfully."



# Configure the SMBv1 client driver
$SMBv1ClientDriverConfig = 0

if ((Get-ItemPropertyValue -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "SMB1") -ne $SMBv1ClientDriverConfig) {
    Write-Host "Configuring SMBv1 client driver..."
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "SMB1" -Value $SMBv1ClientDriverConfig
    Write-Host "SMBv1 client driver configured successfully."
} else {
    Write-Host "SMBv1 client driver is already configured as desired."
}
